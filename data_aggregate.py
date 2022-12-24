import pandas as pd
from os import listdir

FOLDER_PATH = '/Users/Kevin/Documents/GitHub/Research-Renewables_Matching/raw_data/energy_consumption/'

new_df = pd.DataFrame()

for year in range(2015, 2021):
    filenames = listdir(FOLDER_PATH + str(year))
    filenames.sort()

    for filename in filenames:
        if filename.endswith('.csv'):
            df = pd.read_csv(FOLDER_PATH + str(year) + '/' + filename, index_col=0)
            df.drop(labels=['job_type', 'slo'], axis=1, inplace=True)

            new_columns = []
            for i in range(0, 24):
                hour = str(i)
                new_columns.append(filename[:-4] + ' ' + hour.zfill(2) + ':00:00')

            df = df.T
            df.columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            df.insert(0, "datetime", new_columns)
            df.reset_index(drop=True, inplace=True)

            #print(df)

            new_df = new_df.append(df, ignore_index=True)

new_df.to_csv(FOLDER_PATH + 'all.csv')
