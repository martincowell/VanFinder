# from matplotlib import pyplot as plt
# import numpy as np
# import matplotlib

import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd
import json

#sets = {'20180128_cg_FTrans_148_HR': 'black', '20180218_cg_FTrans_148_HR': 'black', '20180311_cg_FTrans_148_HR': 'red'}
sets = {'20180324_cg_FTrans_148_HR_NExt': 'black'}

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

ax.set_xlabel(r'Odometer [mi]', fontsize=15)
ax.set_ylabel(r'Price [$]', fontsize=15)
ax.set_title('VanComparison')
plt.xlim(0, 150000)
plt.ylim(0, 40000)
ax.legend()

plt.savefig('20180324_FTrans_148HR_NExt.pdf')
plt.show()
