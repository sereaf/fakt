# 1
print("1. Feladat")

fajl = input("Adja meg a bemeneti fájl nevét! ")

sor = int(input("Adja meg egy sor számát! "))
while sor < 1 or sor > 9:
    sor = int(input("Adja meg egy sor számát! "))
oszlop = int(input("Adja meg egy oszlop számát! "))
while oszlop < 1 or oszlop > 9:
    oszlop = int(input("Adja meg egy oszlop számát! "))

# 2
print("2. Feladat")

with open(fajl) as f:
    sorok = []
    lepesek = []
    for i, s in enumerate(f):
        if i < 9:
            sorok.append(s.split())
        else:
            lepesek.append(s.split())
            
# 3
print("3. Feladat")

import math

ert = sorok[sor-1][oszlop-1]
if ert == "0":
    print("Az adott helyet még nem töltötték ki.")
else:
    print("Az adott helyen szereplő szám:", ert)

reszo = math.ceil(oszlop / 3)
if sor <= 3:
    if reszo == 1:
        reszc = 1
    elif reszo == 2:
        reszc = 2
    else:
        reszc = 3
elif sor <= 6:
    if reszo == 1:
        reszc = 4
    elif reszo == 2:
        reszc = 5
    else:
        reszc = 6
else:
    if reszo == 1:
        reszc = 7
    elif reszo == 2:
        reszc = 8
    else:
        reszc = 9
print(f"A hely a(z) {reszc} résztáblázathoz tartozik")

# 4
print("4. Feladat")

ossz = 0
for s in sorok:
    for i in s:
        if i == "0":
            ossz += 1
print("Az üres helyek aránya:", ossz/(9*9/100))

# 5
print("5. Feladat")

for lepes in lepesek:
    print(f"A kiválasztott sor: {lepes[1]} oszlop: {lepes[2]} a szám: {lepes[0]}")
    ert = sorok[int(lepes[1])-1][int(lepes[2])-1]
    if ert == "0":
        sorban = lepes[0] in sorok[int(lepes[1])-1]
        oszlopban = False
        for s in sorok:
            if s[int(lepes[2])-1] == lepes[0]:
                oszlopban = True
        if not sorban and not oszlopban:
            print("A lépés megtehető.")
        elif not sorban and oszlopban:
            print("Az adott oszlopban már szerepel a szám.")
        elif sorban and not oszlopban:
            print("Az adott sorban már szerepel a szám.")
    else:
        print("A helyet már kitöltötték.")
