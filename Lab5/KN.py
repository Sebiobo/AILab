from matplotlib import pyplot as plt
from sklearn.datasets import  load_iris
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
import seaborn as sns

iris_data = load_iris()

numar_exemple, dimensiune_caracteristici = iris_data.data.shape
print(f"Numărul de exemple: {numar_exemple}")
print(f"Dimensiunea caracteristicilor: {dimensiune_caracteristici}\n")

print("Denumirile coloanelor (caracteristicilor):")
for name in iris_data.feature_names:
    print(f"- {name}")
print()

print("Numele claselor:")
for target in iris_data.target_names:
    print(f"- {target}")

x = iris_data.data
y = iris_data.target

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

print("Forma subseturilor de date:")
print(f"- X_train (caracteristici antrenare): {x_train.shape}")
print(f"- y_train (etichete antrenare):       {y_train.shape}")
print(f"- X_test (caracteristici testare):    {x_test.shape}")
print(f"- y_test (etichete testare):          {y_test.shape}")

scaler = StandardScaler()

x_train_nescalat=x_train[:3].copy()

x_train_scalat=scaler.fit_transform(x_train)

x_test_scalat=scaler.transform(x_test)

print("Primele 3 exemple ÎNAINTE de scalare:")
print(x_train_nescalat)
print("\nPrimele 3 exemple DUPĂ scalare:")
print(x_train_scalat[:3])

knn=KNeighborsClassifier(n_neighbors=3)

knn.fit(x_train_scalat,y_train)

predictii=knn.predict(x_test_scalat)

acuratete = accuracy_score(y_test, predictii)

print(f"Acuratețea este: {acuratete}")

acurateti = []
valori_k = range(1, 16)

for k in valori_k:
    knn_temp = KNeighborsClassifier(n_neighbors=k)
    knn_temp.fit(x_train_scalat, y_train)
    scor = knn_temp.score(x_test_scalat, y_test)
    acurateti.append(scor)

plt.figure(figsize=(8, 5))
plt.plot(valori_k, acurateti, marker='o', linestyle='dashed', color='b')
plt.title('Acuratețea modelului KNN în funcție de valoarea k')
plt.xlabel('Valoarea lui k')
plt.ylabel('Acuratețe pe setul de test')
plt.xticks(valori_k)
plt.grid(True)
plt.show()

matrice = confusion_matrix(y_test, predictii)

plt.figure(figsize=(6,4))
sns.heatmap(matrice, annot=True, cmap='Blues',
            xticklabels=iris_data.target_names, yticklabels=iris_data.target_names)
plt.title('Matrice de Confuzie (k=3)')
plt.xlabel('Prezis')
plt.ylabel('Real')
plt.show()

print("Raport de clasificare:")
print(classification_report(y_test, predictii, target_names=iris_data.target_names))

plt.figure(figsize=(8, 6))
scatter = plt.scatter(x[:, 2], x[:, 3], c=y, cmap='viridis', edgecolor='k', s=60)

plt.xlabel(iris_data.feature_names[2])
plt.ylabel(iris_data.feature_names[3])
plt.title("Distribuția florilor după dimensiunile petalei")
plt.colorbar(scatter, ticks=[0, 1, 2], format=plt.FuncFormatter(lambda val, loc: iris_data.target_names[int(val)]))
plt.show()

print("\n--- TESTEAZĂ MODELUL CU O FLOARE NOUĂ ---")
print("Introdu dimensiunile (în cm) pentru a afla ce specie este:")
try:
    sl = float(input("Lungime sepală (ex. 5.1): "))
    sw = float(input("Lățime sepală (ex. 3.5): "))
    pl = float(input("Lungime petală (ex. 1.4): "))
    pw = float(input("Lățime petală (ex. 0.2): "))

    floare_noua = [[sl, sw, pl, pw]]
    floare_noua_scalata = scaler.transform(floare_noua)

    predictie_noua = knn.predict(floare_noua_scalata)
    nume_specie = iris_data.target_names[predictie_noua[0]]

    print(f"\n=> Modelul prezice că floarea ta este: **{nume_specie.upper()}**!")

except ValueError:
    print("Te rog să introduci doar numere (folosește punctul pentru zecimale)!")