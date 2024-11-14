import os
import pandas as pd
import numpy as np
import sqlite3

print("Setting up the environment...", end=" ")

if not os.path.isdir('data'):
  os.mkdir('data')

con = sqlite3.connect('data/db')

tsvs = [f for f in  os.listdir() if f.split('.')[-1] == 'tsv']
for tsv in tsvs:
  df = pd.read_csv(tsv, sep='\t')
  x = tsv[:-4]
  df.to_csv(f'data/{x}.csv', index=False)
  df.to_excel(f'data/{x}.xlsx', index=False)
  df.to_sql(x, index=False, con=con, if_exists='replace')

print("Done.")
