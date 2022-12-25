from gym.envs.registration import register
import pandas as pd

#renewables_df = pd.read_csv('C:/Users/Kevin Zheng/Documents/GitHub/Research-Renewables_Matching/data/energy_data.csv', index_col=0)
#datacenter_df = pd.read_csv('C:/Users/Kevin Zheng/Documents/GitHub/Research-Renewables_Matching/data/datacenter_data.csv', index_col=0)

renewables_df = pd.read_csv('/Users/Kevin/Documents/GitHub/Research-Renewables_Matching/data/energy_data.csv', index_col=0)
datacenter_df = pd.read_csv('/Users/Kevin/Documents/GitHub/Research-Renewables_Matching/data/datacenter_data.csv', index_col=0)

register(
    id='renewables_matching-v0',
    entry_point='renewables_matching.envs:MultiAgentEnv',
    kwargs={'renewables_df': renewables_df, 'datacenter_df': datacenter_df},
)
