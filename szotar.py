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


# 4.


import random


lottoszamok = [random.sample(range(1, 91), 5) for _ in range(52)]
print(lottoszamok)
