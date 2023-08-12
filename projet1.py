N = int(input("konbyen not ou vle tape :"))
print("mwen vle tape",N, "not")
lisNote = [0]*N
i=0
som = 0
while i < N :
    tapeNot = float(input("tape not ou :"))
    lisNote[i] = tapeNot
    i+=1
print("men not ou tape yo :",lisNote)
moy = sum(lisNote)/N
print("mwayenn nan se :",moy)
if moy>=90:
    print("ou nan klas A")
elif moy >= 80 and moy < 90:
    print("ou nan klas B")
elif moy >= 70 and moy < 80:
    print("ou nan klas C") 
elif moy >= 60 and moy < 70:
    print("ou nan klas D")
else :
    moy < 60
    print("ou nan klas F")

