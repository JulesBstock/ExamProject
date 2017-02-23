import pandas as pd
import numpy as np
import os

outpath = os.path.abspath('./Results/export.csv')
print(outpath)

if not os.path.exists(os.path.abspath('./Results')):
    os.makedirs('./Results')

df1 = pd.read_csv(outpath, intex_label=False)
print(df1)