import pandas as pd

df=pd.read_csv('data.csv')

df_varsta=df[df['Age']<40]
print(df_varsta.head(10))
