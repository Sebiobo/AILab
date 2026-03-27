data=[10,20,30,40,50]

def normalizare(data):
    val_min = min(data)
    val_max = max(data)

    rezultat=[]
    for x in data:
        nrm=(x-val_min)/(val_max-val_min)
        rezultat.append(nrm)
    return rezultat

print(data)
print(normalizare(data))