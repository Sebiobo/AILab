pare={i for i in range(1,11) if i%2==0}
print(pare)
nume="sebastian"
litere_comune={i for i in nume}
print(f"nume: {nume}")
print(f"litere comune {litere_comune}")
text = "Python este un limbaj de programare versatil si foarte popular in intreaga lume"
x=text.split()
cuvinte=[i for i in x if len(i)>=5]
print(cuvinte)