# from matplotlib import pyplot as plt
# import numpy as np
# import matplotlib

import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd
import json

sets = {'vans_20171231_sprinter': 'black', 'vans_20171231_transit': 'red'}

fig, ax = plt.subplots()
for filename, color in sets.items():
    with open(filename + '.json') as data_file:
        data = json.load(data_file)
    df = pd.DataFrame(data)
    ax.scatter(df.mileages, df.prices, s=12, color=color, alpha=0.3, label=filename)

# with open('vans_20171231_sprinter.json') as data_file:
#     data = json.load(data_file)
#
# df = pd.DataFrame(data)
# print(df)
# print('json complete')
#
# fig, ax = plt.subplots()
# ax.scatter(df.mileages, df.prices, s=12, color='black', alpha='0.5')
#
# ## Plot second set of data
# with open('vans_20171231_transit.json') as data_file:
#     data = json.load(data_file)
#
# df = pd.DataFrame(data)
# print(df)
# print('json complete')
#
# ax.scatter(df.mileages, df.prices, s=12, color='black'), alpha='0.5')

##

ax.set_xlabel(r'mileage', fontsize=15)
ax.set_ylabel(r'price', fontsize=15)
ax.set_title('Mercedes Benz Sprinter Cargo 144 \n cargurus.com')
plt.xlim(0, 250000)
plt.ylim(0, 80000)
ax.legend()

plt.show()
