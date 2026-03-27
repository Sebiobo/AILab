even_list=[i for i in range (100) if i%2==0 ]
print(even_list)
sqr=[i**2 for i in range(1,11)]
print(sqr)
lista_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista_b = [5, 6, 7, 8, 9, 10, 11, 12]
comune=[i for i in lista_a for j in lista_b if i==j]
print(f"prima lista: {lista_a}")
print(f"a doua lista: {lista_b}")
print(f"comune: {comune}")
