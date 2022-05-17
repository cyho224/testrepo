import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

df = pd.read_excel (r'R:\DVCS\UAT and Testing\2022\HKD_Branch.xlsx',skiprows=[0,1,2,3,5],sheet_name='ror-x cf')
df.set_index('Unnamed: 0', inplace =True)
df.index.name = 'Date'
df.columns = list(map(str, df.columns))
avg_return_dm_bonds = df["INV-DM Bonds"].astype("float").mean(axis=0)
print(df[["INV-DM Bonds","XUF","XUM"]].corr())
#DM_bonds = df.loc['INV-DM Bonds']
#print(DM_bonds)
