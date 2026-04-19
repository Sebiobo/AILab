import pandas as pd

df = pd.read_csv('data.csv')

df['Value'] = pd.to_numeric(df['Value'], errors='coerce')
df['Wage'] = pd.to_numeric(df['Wage'], errors='coerce')

df_afacere = df[['Name', 'Wage', 'Value']].copy()

df_afacere['difference'] = df_afacere['Value'] - df_afacere['Wage']

df_afacere = df_afacere.sort_values(by='difference', ascending=False)

print(df_afacere.head(10))