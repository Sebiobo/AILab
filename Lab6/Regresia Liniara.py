import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

#1
diabetes = load_diabetes()

#2
df = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
df["target"] = diabetes.target
print(df.head())

#3
print(diabetes.feature_names)

#4
print(df.describe())

#5
plt.hist(df["bmi"], bins=20)
plt.xlabel("BMI")
plt.ylabel("Frecvență")
plt.title("Histograma caracteristicii BMI")
plt.show()

#6
plt.scatter(df["bmi"], df["age"], c=df["target"])
plt.xlabel("BMI")
plt.ylabel("Vârstă")
plt.title("BMI și vârstă în funcție de target")
plt.colorbar(label="Target")
plt.show()

#7
X = df[["bmi"]]
y = df["target"]

#8
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

#9
model_bmi = LinearRegression()
model_bmi.fit(X_train, y_train)

#10
y_pred = model_bmi.predict(X_test)

plt.scatter(X_test, y_test)
plt.plot(X_test, y_pred)
plt.xlabel("BMI")
plt.ylabel("Scor diabet")
plt.title("Regresie liniară simplă folosind BMI")
plt.show()

#11
mse = mean_squared_error(y_test, y_pred)
print("MSE:", mse)

#12
X2 = df[["bmi", "bp"]]
y2 = df["target"]

X2_train, X2_test, y2_train, y2_test = train_test_split(
    X2, y2, test_size=0.2, random_state=42
)

model_bmi_bp = LinearRegression()
model_bmi_bp.fit(X2_train, y2_train)

#13
print("Coeficient BMI:", model_bmi_bp.coef_[0])
print("Coeficient BP:", model_bmi_bp.coef_[1])

#14
r2 = model_bmi_bp.score(X2_test, y2_test)
print("R²:", r2)