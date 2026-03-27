
nr=int(input("Introduceti cate numere consecutive vreti sa contina lista: "))
my_list=[i+1 for i in range(nr)]
print(my_list)

ptr=lambda my_list: [n**2 for n in my_list]

print(ptr(my_list))