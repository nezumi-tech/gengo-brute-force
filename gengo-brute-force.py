# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 18:29:20 2019

@author: nezum
"""

import pandas as pd

joyo = pd.read_csv("joyo_kanji.csv", header=None)
    
joyo_list = joyo.values.tolist()
    
gengo_list = [] 

for a in range(len(joyo_list) - 1):
    for b in range(len(joyo_list) - 1):
        gengo_list.append(''.join(joyo_list[a] + joyo_list[b]))

gengo = pd.DataFrame(gengo_list)

gengo.to_csv("gengo.csv", header=False, index=False)