import os
import pandas as pd
import numpy as np
import sqlite3

print("Setting up the environment...", end=" ")

types = pd.read_csv("https://raw.githubusercontent.com/pyville-dotcom/datasets/refs/heads/main/store/types.tsv", sep='\t')
colors = pd.read_csv("https://raw.githubusercontent.com/pyville-dotcom/datasets/refs/heads/main/store/colors.tsv", sep='\t')
items = pd.read_csv("https://raw.githubusercontent.com/pyville-dotcom/datasets/refs/heads/main/store/items.tsv", sep='\t')
sales = pd.read_csv("https://raw.githubusercontent.com/pyville-dotcom/datasets/refs/heads/main/store/sales.tsv", sep='\t')

if not os.path.isdir('data'):
  os.mkdir('data')

con = sqlite3.connect('db')

for x in 'types colors items sales'.split():
  df = eval(x)
  df.to_csv(f'data/{x}.csv', index=False)
  df.to_excel(f'data/{x}.xlsx', index=False)
  df.to_sql(x, index=False, con=con, if_exists='replace')

print("Done.")
