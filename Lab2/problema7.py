comentariu=input("introdu un comentariu: ").split()
cpozitiv=["bine", "frumos", "super", "excelent", "minunat"]
cnegativ=["urât", "prost", "groaznic", "dezamăgitor"]


comunep = list(set(comentariu) & set(cpozitiv))
comunen=list(set(comentariu) & set(cnegativ))

if(comunep):
    print("Comentariu pozitiv!")
elif(comunen):
    print("Comentariu negativ!")
else:
    print("Comentariu neutru!")
