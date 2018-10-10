#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 14:13:16 2018

@author: aitorjara
"""

import numpy as np
import geopandas as gpd
from geopandas.tools import sjoin
from matplotlib import pyplot as plt
import pandas as pd
from shapely.geometry import Point
import os
dept_of_interest = 'Dept_37-00027'
dept_fold = '/Users/aitorjara/Documents/GitHub/machine_learning_shared/Kaggle_Datasets_Competitions/data-science-for-good/'+ dept_of_interest + '/' 
census_fold, shape_fold, police_file = os.listdir(dept_fold)

#Have a look at the folder
for file in os.listdir(dept_fold + shape_fold):
    if '.shp' in file:
        shape_file = file
    else: break

# use geopandas to read this file
shape_file_hand = gpd.read_file(dept_fold + shape_fold + '/' + shape_file )
# use geopandas to read the 
prep_file_hand = gpd.read_file(dept_fold + police_file).iloc[1:].reset_index(drop = True)
shape_file_hand.head()
                    
