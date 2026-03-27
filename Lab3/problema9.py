list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]
def sum_lists(list1, list2):
    rezultat=[]
    for el1 ,el2 in zip(list1,list2):
        rezultat.append(el1+el2)
    return rezultat
result = sum_lists(list1, list2)
print(result)