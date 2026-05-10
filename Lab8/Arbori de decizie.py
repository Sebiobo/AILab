import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree

#1
wine = load_wine(as_frame=True)
df = wine.frame

print(df.head())
print(wine.feature_names)

#2
X = df[["alcohol", "flavanoids"]]
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

tree_depth_2 = DecisionTreeClassifier(max_depth=2, random_state=42)
tree_depth_2.fit(X_train, y_train)

plt.figure(figsize=(12, 6))
plot_tree(
    tree_depth_2,
    feature_names=["alcohol", "flavanoids"],
    class_names=wine.target_names,
    filled=True
)
plt.show()

print("Primele noduri conțin condiții pe alcohol/flavanoids.")
print("Clasa prezisă este clasa majoritară din fiecare nod/frunză.")

#3
tree_full = DecisionTreeClassifier(max_depth=None, random_state=42)
tree_full.fit(X_train, y_train)

accuracy_full = tree_full.score(X_test, y_test)
print("Acuratețe arbore complet:", accuracy_full)

#4
X_all = df[wine.feature_names]
y_all = df["target"]

X_all_train, X_all_test, y_all_train, y_all_test = train_test_split(
    X_all, y_all, test_size=0.2, random_state=42
)

tree_all = DecisionTreeClassifier(random_state=42)
tree_all.fit(X_all_train, y_all_train)

importances = pd.DataFrame({
    "feature": wine.feature_names,
    "importance": tree_all.feature_importances_
}).sort_values(by="importance", ascending=False)

print(importances)
print("Cele mai importante caracteristici sunt primele din tabel.")

#5
subset = df[["alcohol", "flavanoids", "target"]].head(6)
print(subset)

total = len(subset)
counts = subset["target"].value_counts()

gini_root = 1
for count in counts:
    p = count / total
    gini_root -= p ** 2

print("Gini impurity pentru nodul rădăcină:", gini_root)

split_value = subset["alcohol"].mean()

left = subset[subset["alcohol"] <= split_value]
right = subset[subset["alcohol"] > split_value]

print("Split propus: alcohol <=", split_value)
print(left)
print(right)

def gini(data):
    total = len(data)
    counts = data["target"].value_counts()

    impurity = 1
    for count in counts:
        p = count / total
        impurity -= p ** 2

    return impurity

gini_left = gini(left)
gini_right = gini(right)

weighted_gini = (len(left) / total) * gini_left + (len(right) / total) * gini_right

print("Gini după split:", weighted_gini)

if weighted_gini < gini_root:
    print("Split-ul este bun, deoarece reduce impuritatea.")
else:
    print("Split-ul nu este bun, deoarece nu reduce impuritatea.")