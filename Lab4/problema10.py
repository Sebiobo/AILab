import pandas as pd

df = pd.read_csv('data.csv')

df['Position'] = df['Position'].fillna('Unknown')


print("Verificare coloană Position:")
print(df[['Name', 'Position']].head(10))