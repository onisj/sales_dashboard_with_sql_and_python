#!/usr/bin/env python
# coding: utf-8

# # Exploratory Data Analysis

# Import libraries
import pandas as pd
import numpy as np
from tabulate import tabulate



# Read the CSVs file into a DataFrame
products = pd.read_csv('data/raw/products.csv')
accounts = pd.read_csv('data/raw/accounts.csv')
sales_teams = pd.read_csv('data/raw/sales_teams.csv')
sales_pipeline = pd.read_csv('data/raw/sales_pipeline.csv')



# Rename products
products['product'] = products['product'].replace({'GTX Plus Basic': 'GTX Basic+', 'GTX Plus Pro': 'GTX Pro+'})

# Changing the `NaN` values to `-`
accounts['subsidiary_of'] = accounts['subsidiary_of'].fillna('-')

# Rename products
sales_pipeline['product'] = sales_pipeline['product'].replace({'GTX Plus Basic': 'GTX Basic+', 'GTX Plus Pro': 'GTX Pro+'})

# Change the date columns to date
sales_pipeline['engage_date'] = pd.to_datetime(sales_pipeline['engage_date'])
sales_pipeline['close_date'] = pd.to_datetime(sales_pipeline['close_date'])

# Deals with missin values
sales_pipeline['account'] = sales_pipeline['account'].fillna('')
sales_pipeline['engage_date'] = sales_pipeline['engage_date'].fillna('')
sales_pipeline['close_date'] = sales_pipeline['close_date'].fillna('')
sales_pipeline['close_value'] = sales_pipeline['close_value'].fillna('')

# Save the Product dataframe to a CSV file
products.to_csv('./data/improved_sql/products.csv', index=False)
sales_pipeline.to_csv('./data/improved_sql/sales_pipeline.csv', index=False)
sales_teams.to_csv('./data/improved_sql/sales_teams.csv', index=False)
accounts.to_csv('./data/improved_sql/accounts.csv', index=False)
