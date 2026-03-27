
print("--- Bine ai venit în Pădurea Magică! ---")
print("Scopul tău este să explorezi și să aduni obiecte magice.")

inventar = []

# Prima decizie
print("\nTe afli la o răscruce. Drumul din stânga pare întunecat, cel din dreapta este plin de flori.")
directie = input("Încotro mergi? (stanga/dreapta): ").lower()

if directie == "stanga":
    print("\nAi ales drumul întunecat. Mergi ce mergi și dai peste un lup somnoros!")
    print("Lângă el strălucește o 'Sabiuta de Argint'.")

    decizie_lup = input("Încerci să iei sabia fără să-l trezești? (da/nu): ").lower()

    if decizie_lup == "da":
        print("Succes! Ai furat sabia și ai fugit repede.")
        inventar.append("Sabiuta de Argint")
    else:
        print("Ai ales să fii prudent și ai ocolit lupul. Nu ai găsit nimic.")

elif directie == "dreapta":
    print("\nDrumul cu flori te duce la o cascadă sclipitoare.")
    print("În apă vezi un 'Inel de Smarald'.")

    decizie_apa = input("Vrei să intri în apă să-l iei? (da/nu): ").lower()

    if decizie_apa == "da":
        print("Apa era caldă și plăcută. Ai obținut inelul!")
        inventar.append("Inel de Smarald")
    else:
        print("Ai stat pe margine și ai admirat peisajul, dar pleci cu mâna goală.")

else:
    print("\nTe-ai pierdut prin mărăcini pentru că nu ai ales o direcție clară.")

print("\n--- SFÂRȘITUL AVENTURII ---")

if len(inventar) > 0:
    print(f"Ai plecat din pădure cu următoarele obiecte: {inventar}")
else:
    print("Nu ai reușit să aduni niciun obiect magic. Poate data viitoare!")