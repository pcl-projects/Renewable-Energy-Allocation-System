import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

FOLDER_PATH = '/Users/Kevin/Documents/GitHub/Research-Renewables_Matching/'

ENERGY_PATH = FOLDER_PATH + 'data/real_generation.csv'
CONSUMPTION_PATH = FOLDER_PATH + 'data/real_consumption_minimal.csv'

generation_df = pd.read_csv(ENERGY_PATH, index_col=0)
consumption_df = pd.read_csv(CONSUMPTION_PATH, index_col=0)
generation_df_2 = pd.read_csv(FOLDER_PATH + 'data/real_generation_2x.csv', index_col=0)
generation_df_3 = pd.read_csv(FOLDER_PATH + 'data/real_generation_3x.csv', index_col=0)

"""
consumption_df.drop(['f', 'j', 'r', 'd', 'i', 'p', 'o', 'q', 'x', 'y', 'g', 'a', 'b', 'k', 'l', 'm', 'u', 'v', 'w'], 1, inplace=True)

new_df = pd.DataFrame()
new_df.insert(0, column='c', value=consumption_df['c'])
new_df.insert(0, column='h', value=consumption_df['h'])
new_df.insert(0, column='n', value=consumption_df['n'])
new_df.insert(0, column='s', value=consumption_df['s'])
new_df.insert(0, column='t', value=consumption_df['t'])
consumption_df.insert(0, 'chnst', value=new_df.sum(axis=1))

new_df = pd.DataFrame()
new_df.insert(0, column='h', value=consumption_df['h'])
new_df.insert(0, column='s', value=consumption_df['s'])
new_df.insert(0, column='t', value=consumption_df['t'])
consumption_df.insert(0, 'hst', value=new_df.sum(axis=1))

consumption_df.drop(['c', 'h', 'n', 's', 't', ], 1, inplace=True)

#consumption_df.to_csv(FOLDER_PATH + 'data/real_consumption_minimal.csv')
"""
"""
for column in columns:
    print('==================================================')
    print(np.mean(generation_df[column]))
    print(np.median(generation_df[column]))
    q1 = np.percentile(generation_df[column], 25)
    q3 = np.percentile(generation_df[column], 75)
    print(q1)
    print(q3)
    max = q3 + 1.5 * (q3 - q1)
    count = 0
    for x in generation_df[column]:
        if x > max:
            count += 1
    print(count)
    print(count /  len(generation_df[column]) * 100)
"""



consumption_df.plot.box(grid='True')
generation_df.plot.box(grid='True')
generation_df_2.plot.box(grid='True')
generation_df_3.plot.box(grid='True')
plt.show()
