import pandas as pd

df = pd.read_csv('data.csv')

df['Value'] = pd.to_numeric(df['Value'], errors='coerce')
df['Wage'] = pd.to_numeric(df['Wage'], errors='coerce')

df['is_underpaid'] = df['Wage'] < (df['Value'] / 100)

coloane_afisate = ['Name', 'Wage', 'Value', 'is_underpaid']
print(df[coloane_afisate].head(10))