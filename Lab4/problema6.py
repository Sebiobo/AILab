import pandas as pd

df = pd.read_csv('data.csv')


print(f"Setul de date are {df.shape[0]} rânduri și {df.shape[1]} coloane.")

jucatori_unici = df['ID'].nunique()
print(f"Avem {jucatori_unici} jucători unici.")