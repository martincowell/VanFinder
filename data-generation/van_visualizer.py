# from matplotlib import pyplot as plt
# import numpy as np
# import matplotlib

import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd

import json

with open('vans1-11_new.json') as data_file:
    data = json.load(data_file)

df = pd.DataFrame(data)
print(df)
print('json complete')

fig, ax = plt.subplots()
ax.scatter(df.mileages, df.prices, s=12, color='black')
ax.set_xlabel(r'mileage', fontsize=15)
ax.set_ylabel(r'price', fontsize=15)
ax.set_title('Mercedes Benz Sprinter Cargo 144 \n cargurus.com')
plt.xlim(0, 250000)
plt.ylim(0, 80000)

plt.show()
