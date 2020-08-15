#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 09:27:08 2020

@author: liuchen
"""

import glassdoor_scraper as gs
import pandas as pd

path = "/Users/liuchen/Desktop/Data_Science/chromedriver"

df = gs.get_jobs('business analyst',950,False,path,15)
df.to_csv('glassdoor_jobs.csv',index = False)
