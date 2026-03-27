patrate={i:i**2 for i in range(1,11)}
print(patrate)
nume1="sebastian"
aparitii={i: nume1.count(i) for i in nume1}
print(f"nume: {nume1}")
print(aparitii)
divizorii={i:[j for j in range(1,i+1)if i%j==0] for i in range(1,11)}
print(divizorii)