import pandas as pd

df=pd.read_csv('data.csv')

df_overall=df[(df['Overall']>=85) & (df['Age']<25)]

print(df_overall)
