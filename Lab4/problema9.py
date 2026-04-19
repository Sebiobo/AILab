import pandas as pd


df = pd.read_csv('data.csv')

df['SprintSpeed'] = pd.to_numeric(df['SprintSpeed'], errors='coerce')
df['Acceleration'] = pd.to_numeric(df['Acceleration'], errors='coerce')

media_atribute = df.groupby('Nationality')[['SprintSpeed', 'Acceleration']].mean()

print(media_atribute.head(15))