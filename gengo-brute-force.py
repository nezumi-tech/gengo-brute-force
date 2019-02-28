# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 18:29:20 2019

@author: nezumi_tech
"""

import pandas as pd
joyo = pd.read_csv("joyo_kanji.csv", header=None)
    
joyo_list = joyo.values.tolist()

with open('gengo.csv', mode='w', encoding='utf-8') as f:
    for a in range(len(joyo_list) - 1):
        for b in range(len(joyo_list) - 1):
            f.write(''.join(joyo_list[a] + joyo_list[b])+'\n')