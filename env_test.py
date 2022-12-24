import gym
import renewables_matching
import pandas as pd

# Import data
renewables_df = pd.read_csv('data/energy_data.csv', index_col=0)
datacenter_df = pd.read_csv('data/datacenter_data.csv', index_col=0)

# Create environment
env = gym.make('renewables_matching-v0', renewables_df=renewables_df, datacenter_df=datacenter_df)

for i in range(0, 50):
    # actions = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    actions = [[i, i, i, i], [i, i, i, i], [i, i, i, i], [i, i, i, i]]
    obs, rewards, done, info = env.step(actions)
    env.render()
