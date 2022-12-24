import pandas as pd
import gym
import renewables_matching
import numpy as np

from stable_baselines.common.policies import MlpPolicy
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines import PPO2
from stable_baselines import A2C


def evaluate(model, num_steps=1000):
    rewards_total = 0
    obs = env.reset()
    for i in range(num_steps):
        # _states are only useful when using LSTM policies
        action, _states = model.predict(obs)
        # here, action, rewards and dones are arrays
        # because we are using vectorized env
        obs, rewards, dones, info = env.step(action)

        # Stats
        rewards_total += rewards[0]
        if dones[0]:
            obs = env.reset()
    # Compute mean reward for the last 100 episodes
    print("Mean reward:", rewards_total / num_steps)

    return rewards_total / num_steps


env = gym.make('renewables_matching-v0')
env = DummyVecEnv([lambda: env])

model = A2C(MlpPolicy, env, verbose=0)

mean_reward_before_train = evaluate(model, num_steps=10000)

model.learn(total_timesteps=500000)

mean_reward = evaluate(model, num_steps=10000)
mean_reward = evaluate(model, num_steps=10000)
mean_reward = evaluate(model, num_steps=10000)
