import pandas as pd


df = pd.read_csv('data.csv')

df['Overall'] = pd.to_numeric(df['Overall'], errors='coerce')

club_top = df.groupby('Club')['Overall'].mean().sort_values(ascending=False).head(1)

print("Clubul cu cel mai mare Overall mediu este:")
print(club_top)