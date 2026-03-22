nota=int(input("introduceti nota:"))

my_list=list(range(1,11))

while nota not in my_list:
    nota=int(input("reintroduceti nota:"))

if nota<5:
    print("reexaminare")
elif nota<7:
    print("suficient")
elif nota <9:
    print("bine")
elif nota <=10:
    print("excelent")