gata = True
def func():
    reguli={
        "piatra": "foarfeca",
        "foarfeca": "hartie",
        "hartie": "piatra"
    }
    return reguli

reguli = func()

while gata:
    jucator1=input("Selectati una dintre optiunile(piatra/hartie/foarfeca): ").lower()
    jucator2=input("Selectati una dintre optiunile(piatra/hartie/foarfeca): ").lower()

    if jucator1 not in reguli and jucator2 not in reguli:
        print("trebuie sa introduceti una din cele 3 ")
        continue
    elif jucator1==jucator2:
        print("Egalitate")
    elif reguli[jucator1]==jucator2:
        print("Jucatorul 1 a castigat")
    else :
        print("Jucatorul 2 a castigat")

    raspuns=input("Doriti sa mai jucati ?").lower()

    if raspuns !="da":
        gata=False
