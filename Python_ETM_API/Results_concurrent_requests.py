# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 15:12:56 2018
Author: frank buters - frank.buters@data-quest.nl
Description: csv to heatmap 
Status: Finished 
"""

import numpy as np
import time
import pandas as pd
import seaborn as sn
from matplotlib import pyplot as plt
from pylab import close

close("all")

def Plot_heatmap(df):
    r""" Using seaborn to plot matrix as heatmap. 
     
     dataframe: pandas dataframe, index will be used for setting y-axis
    
    """    
    yticks = df.index
    keptticks = yticks[::int(len(yticks)/10)]
    yticks = ['' for y in yticks]
    yticks[::int(len(yticks)/10)] = keptticks
    
    xticks = df.columns
    keptticks = xticks[::int(len(xticks)/10)]
    xticks = ['' for y in xticks]
    xticks[::int(len(xticks)/10)] = keptticks
    
    df.fillna(0,inplace = True)
    plt.figure(figsize = (7,4), dpi = 600) 
    sn.heatmap(df.round(2),yticklabels=yticks,xticklabels=xticks, annot=True,square = False, 
                linecolor = 'k', linewidths=.25, fmt='g', cbar  = False)
    plt.yticks(rotation=0) 
    plt.ylabel("Number of threads", fontsize = 12)
    plt.xlabel("Number of calls", fontsize = 12)
    plt.title("Average time per call (seconds)", fontsize = 15)
    plt.tight_layout()
    plt.savefig(r".\Results\Heatmap.png", bbox_inches='tight')
    pass

df = pd.read_csv(r'.\Results\result.csv', header = None)
df.columns = df.columns + 1
df.index = df.index + 1
for i, col in enumerate(df.columns):
    df[col] = df[col]/(i+1)

Plot_heatmap(df)
