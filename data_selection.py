import pandas as pd
import matplotlib.pyplot as plt

FOLDER_PATH = '/Users/Kevin/Documents/GitHub/Research-Renewables_Matching/raw_data/'
CONSUMPTION_PATH = FOLDER_PATH + 'energy_consumption/all.csv'
GENERATION_PATH = FOLDER_PATH + 'energy_generation/all.csv'

generation_df = pd.read_csv(GENERATION_PATH, index_col=0)
to_remove = ['Total', 'Average']
generation_df.drop(to_remove, 1, inplace=True)
print(generation_df.mean(0))
print(generation_df.median(0))

consumption_df = pd.read_csv(CONSUMPTION_PATH, index_col=0)
consumption_df.drop(0, inplace=True)
consumption_df.reset_index(drop=True, inplace=True)
to_remove = ['b', 'd', 'e', 'f', 'g', 'i', 'j', 'l', 'm', 'o', 'p', 'q', 'r', 'u', 'v', 'w', 'x', 'y']
selected = ['a', 'c', 'h', 'k', 'n', 's', 't', 'z']
consumption_df.drop(to_remove, 1, inplace=True)
print(consumption_df.mean(0))
print(consumption_df.median(0))

generation_df.plot.box(grid='True')
consumption_df.plot.box(grid='True')
consumption_df.to_csv('data/real_consumption.csv')
plt.show()
