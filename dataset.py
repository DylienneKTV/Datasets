import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# dataset
setje = pd.read_csv('/Users/dylienneevery/Downloads/Pokemon.csv', sep=',')


# feature engineering

generation = setje['Generation']
names = setje['Name']
total = setje['Total']
atk = setje['Attack']
dfs = setje['Defense']

# programme

# plt.xlabel('total')
# plt.ylabel('generation')
# plt.scatter(total, generation)
# plt.show()

# math with numpy
mean_defense = np.mean(dfs)
sum_hp = np.sum(setje['HP'])

x = atk
y = dfs
ratio = np.divide(x, y)
mean_ratio = np.mean(ratio)


# check-up
print(setje.tail())
print('______')
print(type(setje))
print(mean_defense)
print('______')
print(ratio.head())
print('______')
print(mean_ratio)