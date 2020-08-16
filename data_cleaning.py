#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 20:02:52 2020

@author: liuchen
"""

import pandas as pd
df = pd.read_csv('glassdoor_jobs.csv')

# salary parsing
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_kd = salary.apply(lambda x: x.replace('K','').replace('$',''))

df['min_salary'] = minus_kd.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = minus_kd.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df['min_salary']+df['max_salary'])/2

#company text only
df['company_name'] = df.apply(lambda x: x['Company Name'] if x['Rating'] <0 else x['Company Name'][:-3],axis = 1)

#state field
df['job_state'] = df['Location'].apply(lambda x: x.split(' ')[-1])
df['job_state'] = df['job_state'].apply(lambda x: x.strip() if x.strip().lower() != 'virginia' else 'VA' )
df['job_state'] = df['job_state'].apply(lambda x: x.strip() if x.strip().lower() != 'utah' else 'UT')
df['job_state'] = df['job_state'].apply(lambda x: x.strip() if x.strip().lower() != 'ohio' else 'OH')
df['job_state'] = df['job_state'].apply(lambda x: x.strip() if x.strip().lower() != 'minnesota' else 'MN')
df['job_state'] = df['job_state'].apply(lambda x: x.strip() if x.strip().lower() != 'states' else 'Remote')
df['job_state'] = df['job_state'].apply(lambda x: x.strip() if x.strip().lower() != 'state' else 'Remote')

#age of company
df['age'] = df['Founded'].apply(lambda x: x if x<1 else 2020-x)

#Excel 
df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)

#Sql
df['sql'] = df['Job Description'].apply(lambda x: 1 if 'sql' in x.lower() else 0)

#Python
df['python'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)

#tableau
df['tableau'] = df['Job Description'].apply(lambda x: 1 if 'tableau' in x.lower() else 0)

#word
df['word'] = df['Job Description'].apply(lambda x: 1 if 'word' in x.lower() else 0)

#crm
df['crm'] = df['Job Description'].apply(lambda x: 1 if 'crm' in x.lower() else 0)


df_out = df
df_out.to_csv('data_cleaned.csv',index = False)

pd.read_csv('data_cleaned.csv')

