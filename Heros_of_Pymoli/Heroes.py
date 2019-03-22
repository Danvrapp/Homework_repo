# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 11:09:50 2019

@author: Dan
"""

import pandas as pd
import os

csvpath = 'Heros.csv'
print (os.path.isfile(csvpath))

data_file_pd = pd.read_csv(csvpath)
data_file_pd.head()