def genereaza_factura(args,**kwargs):
    print(f"Factura pentru:{args} ")
    total=0

    for produs,pret in kwargs.items():
        print(f"Produs: {produs}  |  Pret:{pret}")
        total+=pret
    print(f"Factura total:{total}")

genereaza_factura("Sebastian",Laptop=3500, Mouse=150)