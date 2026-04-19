import pandas as pd

df=pd.read_csv('data.csv')

df['Contract Valid Until'] = pd.to_numeric(df['Contract Valid Until'], errors='coerce')

contract=df[df['Contract Valid Until']<2021]

print(contract)


