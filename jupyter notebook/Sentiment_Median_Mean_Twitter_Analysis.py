# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 23:38:11 2021

@author: capt
"""

import scipy
import sys
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

list_of_info = []
list_of_filenames = []


for i in range(104, 107):
    filename = f'corona_tweets_{i}.csv'
    tweets_ds = pd.read_csv(filename, header=None)
    list_of_filenames.append(filename)
    tweets_ds.dropna(inplace=True)
    tweets_ds.columns = ["First", "Second"]
    vals = tweets_ds["Second"]
    vals = vals.to_numpy()
    vals = vals[vals <= -0.05]
    list_of_info.append(vals)
    print(i, vals.mean(), scipy.median(vals), vals.max(), vals.min())
    

with open("guru98.txt","w") as f:
    for count, each in enumerate(list_of_info):
        f.write(f"This is file {list_of_filenames[count]} \n")
        f.write(f"Mean: {str(each.mean())}, Median: {str(scipy.median(each))}, Max: {str(each.max())}, Min: {str(each.min())} \n \n")
