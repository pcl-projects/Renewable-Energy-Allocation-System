import copy
import gym
import random
import pandas as pd
#import warnings
import numpy as np
from gym import spaces

#warnings.filterwarnings('error', category=RuntimeWarning)

MAX_ENERGY = 150.0
MIN_ENERGY = 0.0
MAX_REQUEST = 1000.0
MIN_REQUEST = 0.0
MAX_ENERGY_USE = 300.0
MAX_STEP = 143


class MultiAgentEnv(gym.Env):
    metadata = {
        'render.modes' : ['human']
    }


    def __init__(self, renewables_df, datacenter_df):
        super(MultiAgentEnv, self).__init__()


        # Parse dataframes
        self.renewables = []
        for i in range(0, len(renewables_df.columns)):
            self.renewables.append(renewables_df.iloc[:, i].tolist())
        self.datacenters = []
        for i in range(0, len(datacenter_df.columns)):
            self.datacenters.append(datacenter_df.iloc[:, i].tolist())


        # Time
        self.current_step = 0


        # Agents
        self.n = len(self.datacenters)


        # Actions
        low = []
        high = []
        for i in range(0, len(self.renewables)):
            low.append(MIN_REQUEST)
            high.append(MAX_REQUEST)
        self.action_space = spaces.Box(np.array(low), np.array(high), dtype=np.float32)


        # Observations
        low = []
        high = []
        for i in range(0, len(self.renewables)):
            low.append(MIN_ENERGY)
            high.append(MAX_ENERGY)

        low.append(0)
        high.append(MAX_ENERGY_USE)
        self.observation_space = spaces.Box(np.array(low), np.array(high), dtype=np.float32)



    def calculate_rewards(self, energy_received, actions):
        # Percentage of energy satisfied ranging 0 - 100 exponentially, minus extra requested percentage
        rewards = []
        for i in range(0, self.n):
            # Band-aid for ML algorithm giving negative numbers
            skipped = False
            for k in range(0, len(actions[i])):
                if actions[i][k] < 0:
                    rewards.append(0)
                    skipped = True
                    break
            if skipped:
                continue

            total_requested = sum(actions[i])
            reward = 100 * energy_received[i] / self.datacenters[i][self.current_step]

            if reward >= 100:
                reward = 100
            elif reward < 0:
                reward = 0
            else:
                reward = pow(reward, 1.0472)

            extra = total_requested - self.datacenters[i][self.current_step]
            if extra < 0:
                extra = 0

            reward -= 100 * extra / self.datacenters[i][self.current_step]

            rewards.append(reward)


        return rewards

    def get_agent_observations(self):
        # Get energy generation of current step, then append energy need
        curr_energy = []
        for i in range(0, len(self.renewables)):
            curr_energy.append(self.renewables[i][self.current_step])

        obs = []
        for i in range(0, self.n):
            temp = copy.deepcopy(curr_energy)
            temp.append(self.datacenters[i][self.current_step])
            obs.append(np.asarray(temp))


        self.last_obs = obs

        return obs



    def step(self, actions):
        # Execute one time step within the environment
        # Band-aid for nan and inf
        for i in range(0, len(actions)):
            if not np.isfinite(actions[i]):
                print('caught')
                actions[i] = -1.23

        agent_actions = actions
        actions = []
        actions.append(agent_actions)

        #Append steady actions for other agents
        for i in range(1, self.n):
            to_add = []
            for k in range(0, len(self.renewables)):
                to_add.append(self.datacenters[i][self.current_step] * 2 / 3)
            actions.append(to_add)

        self.last_actions = actions

        done = False
        if self.current_step > MAX_STEP - 2:
            done = True

        # Calculate energy received by each datacenter
        energy_given = []
        for i in range(0, len(self.renewables)):
            energy_given.append([])
            total_requested = 0
            for k in range(0, self.n):
                total_requested += actions[k][i]
            for k in range(0, self.n):
                if self.renewables[i][self.current_step] == 0 or total_requested == 0:
                    energy_given[i].append(0)
                else:
                    energy_given[i].append(actions[k][i] / total_requested * self.renewables[i][self.current_step])

        self.energy_received = []
        for i in range(0, self.n):
            total_received = 0
            for k in range(0, len(energy_given)):
                total_received += energy_given[k][i]

            self.energy_received.append(total_received)


        # Calculate rewards
        self.rewards = self.calculate_rewards(self.energy_received, actions)

        # Increment step and check if end of data
        self.current_step += 1

        return self.get_agent_observations()[0], self.rewards[0], done, {}



    def reset(self):
        # Reset the state of the environment to an initial state
        self.current_step = random.randint(0, MAX_STEP - 2)

        return self.get_agent_observations()[0]



    def render(self, mode='human', close=False):
        # Render the environment to the screen
        print('Results From Step: ', self.current_step - 1)
        print('Renewables: ', self.renewables[0][self.current_step - 1], self.renewables[1][self.current_step - 1], self.renewables[2][self.current_step - 1], self.renewables[3][self.current_step - 1])
        print('D1', self.datacenters[0][self.current_step - 1], self.energy_received[0], self.last_actions[0])
        print('D2', self.datacenters[1][self.current_step - 1], self.energy_received[1], self.last_actions[1])
        print('D3', self.datacenters[2][self.current_step - 1], self.energy_received[2], self.last_actions[2])
        print('Rewards: ', self.rewards)
        print('--------------------------------------------------')
