import cProfile
import numpy as np


def np_sum(lst):
    for i in range(0, 1000):
        tst = np.sum(lst, 0)

def lst_comp(lst):
    for i in range(0, 1000):
        tst = [sum(x) for x in zip(*lst)]

lst = []

for i in range(0, 50):
    lst.append([])
    for k in range(0, 500):
        lst[i].append(i + k)

#print(lst)
#print(np_sum(lst))
#print(lst)
#print(lst_comp(lst))
#print(lst)

cProfile.run('np_sum(lst)')
cProfile.run('lst_comp(lst)')
