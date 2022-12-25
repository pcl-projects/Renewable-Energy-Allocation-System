import random
import pandas as pd
import numpy as np

PATH1 = '~/Documents/GitHub/Research-Renewables_Matching/data/real_consumption_minimal.csv'
PATH2 = '~/Documents/GitHub/Research-Renewables_Matching/data/real_generation.csv'

df1 = pd.read_csv(PATH1, index_col=0)
df2 = pd.read_csv(PATH2, index_col=0)

NUM_D_ORIG = 3
NUM_G_ORIG = 5
ENERGY_COPIES = 1
CONSUMPTION_COPIES = 1

bench = ['G1', 'G2', 'G3', 'G4', 'G5', 'D1', 'D2', 'D3',
    'D1A1', 'D1A2', 'D1A3', 'D1A4', 'D1A5',
    'D2A1', 'D2A2', 'D2A3', 'D2A4', 'D2A5',
    'D3A1', 'D3A2', 'D3A3', 'D3A4', 'D3A5',
    'R1', 'R2', 'R3', 'S1', 'S2', 'S3',
    'A1', 'A2', 'A3']

cols = []

for i in range(1, NUM_G_ORIG * ENERGY_COPIES + 1):
    cols.append('G' + str(i))
for i in range(1, NUM_D_ORIG * CONSUMPTION_COPIES + 1):
    cols.append('D' + str(i))
for i in range(1, NUM_D_ORIG * CONSUMPTION_COPIES + 1):
    for k in range(1, NUM_G_ORIG * ENERGY_COPIES + 1):
        cols.append('D' + str(i) + 'G' + str(k))
for i in range(1, NUM_D_ORIG * CONSUMPTION_COPIES + 1):
    cols.append('R' + str(i))
for i in range(1, NUM_D_ORIG * CONSUMPTION_COPIES + 1):
    cols.append('S' + str(i))
for i in range(1, NUM_D_ORIG * CONSUMPTION_COPIES + 1):
    cols.append('A' + str(i))

print(bench)
print(cols)

"""
print(df2)

for column in df2.columns:
    lst = df2[column].tolist()
    res = [4 * x for x in lst]
    df2[column] = res

print(df2)
df2.to_csv('~/Documents/GitHub/Research-Renewables_Matching/data/real_generation_4x.csv')
"""

#print(df1)
#print(df2)
#print(df1.min())
#print(max(df1.max()))
#print(df1.mean())
#print(df1.median())
#print(max(df2.max()))
#print(df2.mean())
#print(df2.median())



"""
can_meet = 0
overall_satisfaction = []
diff = []
diff_under = []
iterations = 100000

for i in range(0, iterations):
    generation = 3 * sum(df2.loc[random.randint(0, 43300)]) * 2
    consumption = 3 * sum(df1.loc[random.randint(0, 43300)])

    if generation > consumption:
        can_meet += 1
        overall_satisfaction.append(1.0)
        diff_under.append((generation - consumption) / generation)
    else:
        diff.append((consumption - generation) / generation)
        overall_satisfaction.append(generation / consumption)

print('5x')
print('Percentage Can Be Met: ' + str(can_meet / iterations * 100))
print('Percentage over if over: ' + str(np.mean(diff) * 100))
print('Percentage under if under: ' + str(np.mean(diff_under) * 100))
print('Overall Satisfaction: ' + str(np.mean(overall_satisfaction)))
"""


"""
columns = df1.columns

for column in columns:
    lst = df1[column].tolist()
    for i in range(0, len(lst)):
        if lst[i] < 0:
            print(column + '-' + str(i))
"""
