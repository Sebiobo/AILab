import pandas as pd

df = pd.read_csv('data.csv')

df['Value'] = pd.to_numeric(df['Value'], errors='coerce')
df['Wage'] = pd.to_numeric(df['Wage'], errors='coerce')

jucatori_profitabili = df[df['Value'] > df['Wage']]

numar_jucatori = jucatori_profitabili.shape[0]

print(f"{numar_jucatori} jucători au valoarea mai mare decât salariul.")