import pandas as pd
from bokeh.plotting import figure, show
from bokeh.models import HoverTool, ColumnDataSource

df = pd.read_csv('data.csv')


def curata_bani(valoare):
    if pd.isna(valoare):  # Dacă nu există nicio valoare
        return 0

    valoare = str(valoare).replace('€', '')  # Ștergem simbolul €

    if 'M' in valoare:
        return float(valoare.replace('M', '')) * 1000000  # Înmulțim pentru milioare
    elif 'K' in valoare:
        return float(valoare.replace('K', '')) * 1000  # Înmulțim pentru mii
    else:
        return float(valoare)


df['Value'] = df['Value'].apply(curata_bani)
df['Wage'] = df['Wage'].apply(curata_bani)

df_afacere = df[['Name', 'Wage', 'Value']].copy()
df_afacere['difference'] = df_afacere['Value'] - df_afacere['Wage']
df_afacere = df_afacere.sort_values(by='difference', ascending=False)

top_100_jucatori = df_afacere.head(100)

# ==========================================
#  BONUS
# ==========================================

sursa_date = ColumnDataSource(top_100_jucatori)

p = figure(title="Grafic Interactiv: Value vs Wage (Top 100 Afaceri)",
           x_axis_label='Salariu (Wage)',
           y_axis_label='Valoare (Value)')

p.scatter(x='Wage', y='Value', source=sursa_date, size=10, color="navy", alpha=0.6)

hover = HoverTool(tooltips=[
    ("Jucător", "@Name"),
    ("Valoare", "@Value{0,0} €"),
    ("Salariu", "@Wage{0,0} €"),
    ("Diferență", "@difference{0,0} €")
])

p.add_tools(hover)

show(p)