import random

loto_list = random.sample(range(1, 50), 6)

print("Bine ai venit la Loteria Python!")
print("Alege 6 numere între 1 și 49.")

numbers_list = []
while len(numbers_list) < 6:
    try:
        nr = int(input(f"Numărul {len(numbers_list) + 1}: "))

        if 1 <= nr <= 49 and nr not in numbers_list:
            numbers_list.append(nr)
        else:
            print("Te rugăm să introduci un număr valid (1-49) care nu a fost deja ales.")
    except ValueError:
        print("Introdu un număr valid!")

comune = list(set(loto_list) & set(numbers_list))
nrmatch = len(comune) 


print("-" * 20)
print(f"Numere extrase: {loto_list}")
print(f"Ai ghicit {nrmatch} numere: {comune}")

if nrmatch == 6:
    print("EXTREM! Ai câștigat marele premiu!")
elif nrmatch >= 3:
    print("Felicitări! Ai câștigat un premiu mic!")
else:
    print("Mai încearcă, astăzi nu a fost ziua ta norocoasă.")