import random

secret_number = random.randint(1,50)
incercari=0

while True:
    nr=int(input("introduce un numar intre 1 si 50 "))
    incercari=incercari+1
    if nr>secret_number:
        print("Numarul este mai mic")
    if nr<secret_number:
        print("Numarul este mai mare")
    elif nr==secret_number:
        print("ai ghicit")
        print(incercari)
        break