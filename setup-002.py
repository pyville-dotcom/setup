import os
import pandas as pd
import numpy as np
import sqlite3

if not os.path.isdir('data'):
  os.mkdir('data')

con = sqlite3.connect('data/db')

dtype = {
    'sales': 'INT',
    'store': 'CAHR(3)',
    'city': 'VARCHAR(50)',
    'country': 'VARCHAR(50)',
    'continent': 'VARCHAR(50)',
}

tsvs = [f for f in  os.listdir() if f.split('.')[-1] == 'tsv']

for tsv in tsvs:
  df = pd.read_csv(tsv, sep='\t')
  x = tsv[:-4]
  df.to_csv(f'data/{x}.csv', index=False)
  df.to_excel(f'data/{x}.xlsx', index=False)
  df.to_sql(x, index=False, con=con, if_exists='replace', dtype=dtype)
