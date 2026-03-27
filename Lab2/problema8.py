csus=["Coreea de Nord", "Siria", "Iran"]

nrS=0

while nrS<3:
    suma =int(input("introduceti suma: "))
    tara=input("introduceti tara: ").title()
    if tara in csus:
        nrS+=1
    if suma>10000:
        nrS+=1
print("ati depasit numar de tranzactii suspecte , Cont Blocat")