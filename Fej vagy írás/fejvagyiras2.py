# 1
print("1. Feladat")

import random

szam = random.randint(1, 2)
if szam == 1:
    print("Fej")
else:
    print("Írás")

# 2

print("2. Feladat")

tipp = input("Tipp: ")
szam = random.randint(1, 2)
if szam == 1:
    fejvagyiras = "F"
else:
    fejvagyiras = "I"

print(tipp)
print(fejvagyiras)

if tipp == fejvagyiras:
    print("Ön eltalálta.")
else:
    print("Ön nem találta el.")

# 3

print("3. Feladat")

fajl = open("kiserlet.txt")
ossz = 0
for sor in fajl:
    ossz += 1
fajl.close()
print(f"Összesen {ossz} dobásból állt a kisérlet")

# 4

print("4. Feladat")

fajl = open("kiserlet.txt")
fejossz = 0
ossz = 0
for sor in fajl:
    if sor.strip() == "F":
        fejossz += 1
    ossz += 1
fajl.close()
print("%.2f" % (fejossz / ossz * 100), "% relatív  gyakorisággal  dobtunk  a  kísérlet  során  fejet")

# 5
"""
print("5. Feladat")

fajl = open("kiserlet.txt")
elozo = ""
ossz = 0
for sor in fajl:
    if elozo == "F":
        if sor.strip() == "F":
            ossz += 1
            elozo = ""
    else:
        elozo = sor.strip()
fajl.close()
print(f"A kisérlet során {ossz} alkalommal dobtak pontosan kettőt.")
"""
"""
print("5. Feladat")

fajl = open("kiserlet.txt")
elozo = ""
ossz = 0
for sor in fajl:
    if elozo == "F":
        if sor.strip() == "F":
            elozo += "F"
    elif elozo == "FF":
        if sor.strip() == "I":
            ossz += 1
        elozo = ""
    elif elozo == "I":
        if sor.strip() == "F":
            elozo += "F"
        else:
            elozo = ""
    else:
        elozo = sor.strip()
fajl.close()
print(f"A kisérlet során {ossz} alkalommal dobtak pontosan kettőt.")
"""
# 6

print("6. Feladat")

fajl = open("kiserlet.txt")
elozo = ""
ossz = 0
leghosszabb = 0
for i, sor in enumerate(fajl):
    if elozo == "F":
        if sor.strip() == "F":
            ossz += 1
        else:
            if ossz > leghosszabb:
                leghosszabb = ossz
            ossz = 0
    else:
        elozo = sor.strip()
fajl.close()
print(leghosszabb, " hosszú  volt  a  leghosszabb,  csak  fejekből  álló  részsorozat.")

# 7

print("7. Feladat")
import random

def dob():
    return "I" if random.randint(1, 2) == 1 else "F"

raktar = []

for i in range(1000):
    sorozat = ''
    for dobas in range(4):
        sorozat += dob()
    raktar.append(sorozat)
idb = 0
fdb = 0
for sorozat in raktar:
    if sorozat == "FFFF":
        fdb += 1
    if sorozat == "FFFI":
        idb += 1

with open("dobasok.txt", "w") as dobasok:
    print(f"FFFF: {fdb} db, FFFI: {idb} db", file=dobasok)
    for sorozat in raktar:
        print(sorozat, end=" ", file=dobasok)
    
