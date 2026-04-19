import pandas as pd

df = pd.read_csv('data.csv')

coloane_scor = ['Overall', 'Potential', 'SprintSpeed', 'ShortPassing']
for col in coloane_scor:
    df[col] = pd.to_numeric(df[col], errors='coerce')

df['Scor_Personalizat'] = (0.3 * df['Overall']) + (0.3 * df['Potential']) + (0.2 * df['SprintSpeed']) + (0.2 * df['ShortPassing'])

cei_mai_buni = df.sort_values(by='Scor_Personalizat', ascending=False)
print(cei_mai_buni[['Name', 'Scor_Personalizat']].head())