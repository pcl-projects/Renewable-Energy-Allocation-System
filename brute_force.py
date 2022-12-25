import pandas as pd


def calculate_rewards(energy_received, actions):
    # Percentage of energy satisfied ranging 0 - 100 exponentially, minus extra requested percentage
    global num_datacenters
    global datacenters
    global current_step

    rewards = []
    for i in range(0, num_datacenters):
        total_requested = sum(actions[i])
        reward = 100 * energy_received[i] / datacenters[i][current_step]

        if reward >= 100:
            reward = 100
        elif reward < 0:
            reward = 0
        else:
            reward = pow(1.0472, reward)

        extra = total_requested - datacenters[i][current_step]
        if extra < 0:
            extra = 0

        reward -= 100 * extra / datacenters[i][current_step]

        rewards.append(reward)

    return rewards


def calculate_energy_received(actions):
    global num_datacenters
    global num_renewables
    global datacenters
    global current_step

    energy_given = []
    for i in range(0, num_renewables):
        energy_given.append([])
        total_requested = 0
        for k in range(0, num_datacenters):
            total_requested += actions[k][i]
        for k in range(0, num_datacenters):
            if renewables[i][current_step] == 0 or total_requested == 0:
                energy_given[i].append(0)
            else:
                energy_given[i].append(actions[k][i] / total_requested * renewables[i][current_step])

    energy_received = []
    for i in range(0, num_datacenters):
        total_received = 0
        for k in range(0, num_renewables):
            total_received += energy_given[k][i]

        energy_received.append(total_received)

    return energy_received


PATH1 = '/Users/Kevin/Documents/GitHub/Research-Renewables_Matching/data/energy_data.csv'
PATH2 = '/Users/Kevin/Documents/GitHub/Research-Renewables_Matching/data/datacenter_data.csv'
PATH3 = '/Users/Kevin/Documents/GitHub/Research-Renewables_Matching/data/optimal.csv'

renewables_df = pd.read_csv(PATH1, index_col=0)
datacenter_df = pd.read_csv(PATH2, index_col=0)

renewables = []
for i in range(0, len(renewables_df.columns)):
    renewables.append(renewables_df.iloc[:, i].tolist())

datacenters = []
for i in range(0, len(datacenter_df.columns)):
    datacenters.append(datacenter_df.iloc[:, i].tolist())

num_datacenters = len(datacenters)
num_renewables = len(renewables)
max = len(datacenters[0])

optimals = []

for current_step in range(0, max):
    print('current_step: ', current_step)
    best = 0
    best_actions = []

    for w in range(15, 85):
        print('w: ', w)
        for x in range(15, 85):
            print('x: ', x)
            for y in range(15, 85):
                print('y: ', y)
                for z in range(15, 85):
                    print('z: ', z)
                    for a in range(15, 85):
                        print('a: ', a)
                        for b in range(15, 85):
                            print('b: ', b)
                            for c in range(15, 85):
                                print('c: ', c)
                                for d in range(15, 85):
                                    print('d: ', d)
                                    for h in range(15, 85):
                                        for i in range(15, 85):
                                            for j in range(15, 85):
                                                for k in range(15, 85):
                                                    actions = [[w, x, y, z], [a, b, c, d], [h, i, j, k]]

                                                    energy_given = []
                                                    for i in range(0, num_renewables):
                                                        energy_given.append([])
                                                        total_requested = 0
                                                        for k in range(0, num_datacenters):
                                                            total_requested += actions[k][i]
                                                        for k in range(0, num_datacenters):
                                                            if renewables[i][current_step] == 0 or total_requested == 0:
                                                                energy_given[i].append(0)
                                                            else:
                                                                energy_given[i].append(actions[k][i] / total_requested * renewables[i][current_step])

                                                    energy_received = []
                                                    for i in range(0, num_datacenters):
                                                        total_received = 0
                                                        for k in range(0, num_renewables):
                                                            total_received += energy_given[k][i]

                                                        energy_received.append(total_received)


                                                    rewards = []
                                                    for i in range(0, num_datacenters):
                                                        total_requested = sum(actions[i])
                                                        reward = 100 * energy_received[i] / datacenters[i][current_step]

                                                        if reward >= 100:
                                                            reward = 100
                                                        elif reward < 0:
                                                            reward = 0
                                                        else:
                                                            reward = pow(1.0472, reward)

                                                        extra = total_requested - datacenters[i][current_step]
                                                        if extra < 0:
                                                            extra = 0

                                                        reward -= 100 * extra / datacenters[i][current_step]

                                                        rewards.append(reward)

                                                    total = sum(rewards)

                                                    if total > best:
                                                        best = total
                                                        best_actions = actions

    optimals.append([best, best_actions[0], best_actions[1], best_actions[2]])

data = pd.dataframe(optimals, colums=['Total', 'D1', 'D2', 'D3'])
data.to_csv(PATH3)
print(data)
