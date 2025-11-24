import pandas as pd
import matplotlib.pyplot as plt

#I used AI to convert given picture to .csv file or it would take too long to type everything

df = pd.read_csv("sales.csv")

plt.plot(df['month_number'], df['total_profit'])
plt.show()

plt.plot(df['month_number'], df['total_profit'], linestyle=':', marker='o',
         markerfacecolor='red', markeredgecolor='black', linewidth=3)
plt.show()

products = ['facecream','facewash','toothpaste','bathingsoap','shampoo','moisturizer']
for p in products:
    plt.plot(df['month_number'], df[p], marker='o', linewidth=3, label=p)
plt.legend()
plt.show()

import numpy as np
x = np.arange(len(df))
plt.bar(x-0.2, df['facecream'], 0.4, label='facecream')
plt.bar(x+0.2, df['facewash'], 0.4, label='facewash')
plt.xticks(x, df['month_number'])
plt.legend()
plt.show()