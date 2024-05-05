"""
# szótár adatszerkezet
# 1. lehetőség
bevasarlolista = {
    "alma": 2,
    "körte": 1,
    "dinnye": 5,
    "banán": 2
    }

# 2. lehetőség

bevasarlol = dict()
bevasarlol["krumpli"] = 2
bevasarlol["hagyma"] = 3
bevasarlol["káposza"] = 4

# 3. lehetőség
bevarol = dict([("alma", 2),
    ("körte", 1),
    ("dinnye", 5),
    ("banán", 2)
    ])

print(bevasarlolista)
print(bevasarlol)
print(bevarol)

# elemek elérése

print(len(bevasarlolista))
print(bevasarlol["káposza"])
print("dinnye" in bevarol)
del bevarol["körte"]
print(bevarol)

# iterálás a szótáron

for kulcs in bevasarlolista:
    ertek = bevasarlolista[kulcs]
    print(kulcs, ertek)

for kulcs, ertek in bevasarlolista.items():
    print(f"{kulcs}: {ertek} kg")
"""
"""
diak = {"vezeteknev": "Kiss",
        "keresztnev": "Péter",
        "eletkor": 17,
        "menza": True,
        "lottoszamok": [1, 2, 3, 4, 5]
        }

print(diak["eletkor"])
diak["eletkor"] = 21
print(diak["eletkor"])

diak["osztaly"] = "11.zs"
print(diak)
"""
# 1.
"""
nev = input("Neve: ")
kor = int(input("Életkor: "))
fajtaja = input("Fajtája: ")
oltas = input("Veszettség elleni oltás: ")

adatok = {
    "nev": nev,
    "kor": kor,
    "fajtája": fajtaja,
    "oltás": oltas
    }
print(adatok)
"""

# 2.
"""
macska  = {
    "nev": "^°_°^||||||~~~",
    "kor": 0.0001
    }

kerdes = input("Nev vagy kor?: ")
if kerdes == "nev":
    print(macska["nev"])
    macska["nev"] = input("Módosítsa: ")
elif kerdes == "kor":
    print(macska["kor"])
    macska["kor"] = input("Módosítsa: ")

print(macska)
"""

# 3
"""
a = {
    "a": "a",
    "b": 1,
    "c": False,
    }
print(a)
for i in range(2):
    kulcs = input("Kulcs: ")
    ertek = input("Érték: ")
    a[kulcs] = ertek
print(a)
"""
# 5.
"""
allatok = []

while True:
    allat = {}
    nev = input("Mi az állat neve? ")
    if not nev:
        break
    allat["név"] = nev
    allat["faj"] = input("Mi az állat faja? ")
    allat["szulev"] = 2022 - int(input("Hány éves az állat? "))
    allatok.append(allat)
                
print(allatok)
"""

# 1.
"""
mondat = "Kenyeret ettem meggyel"

lista = [szo.upper() for szo in mondat.split()]

print(lista)
"""
# 2.
"""
import random

lista1 = [random.randint(1, 10) + random.choice([1, -1]) for _ in range(15)]
print(lista1)
"""

# 3.
"""
import math

ossz = 0
for i in range(100):
    if i % 7 == 0:
        ossz += math.sqrt(i)
print(f"{ossz:.2f}")
"""
# 4.
"""
import random

lottoszamok = [random.sample(range(1, 91), 5) for _ in range(52)]
print(lottoszamok)
"""

# 1
"""
import random

tarolo = [[random.randint(0, 25) for a in range(3)] for i in range(4)]

print(tarolo)
"""

# 2
"""
x = 0
y = 0
while x >= 0 and x <= 2 and y >= 0 and y <= 2:
    x = int(input("Koordináta x: "))
    y = int(input("Koordináta y: "))
    if x >= 0 and x <= 2 and y >= 0 and y <= 2:
        tarolo = [["+ " if a == x and i == y else "O " for a in range(3)] for i in range(3)]
        for i in tarolo:
            print("".join(i))
"""

# 3
"""
fajl = open("a.txt")

for sor in fajl:
    print(sor.split()[0], end=", ")

csapat = []
for sor in fajl:
    csapat.append(sor.split()[0])

print(", ".join(csapat))
fajl.close()
"""

# 4
"""
fajl = open("a.txt")
ossz = 0
for sor in fajl:
    if sor.split()[1] == "csatar":
        ossz += 1
print(ossz, "csatár van")
fajl.close()
"""

# 5
"""
poszt = input("Egy poszt: ")
fajl = open("a.txt")

def megszamposzt(lista, poszt):
    ossz = 0
    for sor in lista:
        if sor.split()[1] == poszt:
            ossz += 1
    print(ossz, poszt, "van")


megszamposzt(fajl, poszt) 

fajl.close()
"""

# 6
"""
fajl = open("a.txt")
csapat = []
for sor in fajl:
    csapat.append(sor.split())

legkisebb = csapat[0]
for a in csapat:
    if int(a[-1]) < int(legkisebb[-1]):
        legkisebb = a
print(legkisebb[0], "rúgta a legkevesebb gólt,", legkisebb[1], "poszton.")
fajl.close()
"""

# 7
"""
fajl = open("a.txt")
csapat = []
for sor in fajl:
    csapat.append(sor.split())

for a in csapat:
    if int(a[2]) >= 10:
        print(a[0], "legalább 10 meccset játszott.")
fajl.close()
"""

# 8
"""
fajl = open("a.txt")
csapat = []
for sor in fajl:
    csapat.append(sor.split())

ossz = 0
for a in csapat:
    ossz += int(a[-1])
print(f"{ossz / len(csapat)} gólt rúgtak a játékosok átlagosan")


fajl.close()
"""

# 9
"""
fajl = open("a.txt")
csapat = []
for sor in fajl:
    csapat.append(sor.split())

hatved = 0
hatvedgol = 0
csatar = 0
csatargol = 0
kozeppalyas = 0
kozeppalyasgol = 0
for a in csapat:
    if a[1] == "hatved":
        hatved += 1
        hatvedgol += int(a[-1])
    elif a[1] == "csatar":
        csatar += 1
        csatargol += int(a[-1])
    elif a[1] == "kozeppalyas":
        kozeppalyas += 1
        kozeppalyasgol += int(a[-1])

print(f"A hatvedek {hatvedgol / hatved} gólt rúgtak átlagosan")
print(f"A csatarok {csatargol / csatar} gólt rúgtak átlagosan")
print(f"A kozeppalyasok {kozeppalyasgol / kozeppalyas} gólt rúgtak átlagosan")

fajl.close()
"""

