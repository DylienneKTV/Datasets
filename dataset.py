import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
#
# # dataset
# setje = pd.read_csv('/Users/dylienneevery/Downloads/Pokemon.csv', sep=',')
#
#
# # feature engineering
#
# generation = setje['Generation']
# names = setje['Name']
# total = setje['Total']
# atk = setje['Attack']
# dfs = setje['Defense']
#
# # programme
#
# plt.xlabel('total')
# plt.ylabel('generation')
# # plt.scatter(total, generation)
# # plt.show()
#
# # math with numpy
# mean_defense = np.mean(dfs)
# sum_hp = np.sum(setje['HP'])
#
# x = atk
# y = dfs
# ratio = np.divide(x, y)
# mean_ratio = np.mean(ratio)
#
#
# # check-up
# print(setje.tail())
# print('______')
# print(type(setje))
# print(mean_defense)
# print('______')
# print(ratio.head())
# print('______')
# print(mean_ratio)


# US births 2000-2014

# f = pd.read_csv('US_births_2000-2014_SSA.csv', sep=',')

# for i in f:
#     blabla
#     print(i)
#
# result = "the average of births in usa is %d in 2015"
# print(" result ") %average of 2015


f = open('US_births_2000-2014.csv', 'r')
file = f.read
print(f)

# year = ['US_births_2000-2014_SSA.csv', 'year']
# births = ['US_births_2000-2014_SSA.csv', 'births']
# mean = mean("births")
# if year is "2000":
#     print(mean)



# mean = np.mean("US_births_2000-2014_SSA.csv"[0:368])
# print(mean)

# US_births = "US_births_2000-2014_SSA.csv"[0:368]
# total = np.sum(US_births)
# print(total)

births_2000 = []
for i in "US_births_2000-2014.csv":
    found = i in "US_births_2000-2014.csv"
    births_2000.append(found)
print(births_2000)