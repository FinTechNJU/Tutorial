# -*- coding: utf-8 -*-
"""
Created on Fri May  8 12:20:47 2020

@author: -
"""

import pandas as pd # 用于数据处理
from WindPy import w # 用于打开wind

import matplotlib.pyplot as plt # 用于画图


#pd.read_excel("draw.xlsx",sheet_name='')
w.start()  # 用于打开wind


df1 = w.wsd("000001.SH", "close", "2019-01-01", "2019-12-31", usedf=True)[1]
df2 = w.wsd("000001.SH", "close", "2020-01-01", "2020-04-30", usedf=True)[1]

df = w.wsd("000001.SH", "close", "2019-01-01", "2020-04-30", usedf=True)[1]

#fig = plt.figure()
plt.plot(df1.index, df1.CLOSE)
plt.plot(df2.index, df2.CLOSE)

plt.plot(df.index[:-len(df2)], df.CLOSE.iloc[:-len(df2)])
plt.plot(df.index[len(df1):], df.CLOSE.iloc[len(df1):])
plt.show()

#plt.figure(figsize=(200, 80))

w.stop()  # 用于关闭wind

