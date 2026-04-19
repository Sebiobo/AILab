import pandas as pd

df=pd.read_csv('data.csv')

skill_move=df.sort_values(by=('Skill Moves'), ascending=False)


print(skill_move)
