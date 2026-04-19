import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('data.csv')

top_5_nationalitati = df['Nationality'].value_counts().head(5)

top_5_nationalitati.plot(kind='pie', autopct='%1.1f%%', figsize=(8, 8), title='Top 5 Naționalități')

plt.ylabel('')
plt.show()