import pandas as pd


df = pd.read_csv('data.csv')

top_5_nationalitati = df['Nationality'].value_counts().head(5)

print("Top 5 naționalități:")
print(top_5_nationalitati)