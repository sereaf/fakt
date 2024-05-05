# 1.1, 1.2, 1.3
"""
szamok = []
szam = ""
while szam.lower() != "x":
    szam = input("Egy szám: ")
    if szam.lower() != "x":
        szamok.append(int(szam))

print(szamok)

legkisebb = szamok[0]
legnagyobb = szamok[0]

for sz in szamok:
    if sz % 2 == 0:
        if sz > legnagyobb:
            legnagyobb = sz

        if sz < legkisebb:
            legkisebb = sz
        
print("A legnagyobb szám:", legnagyobb)
print("A legkisebb szám:", legkisebb)
"""


# 2.
"""
szavak = []
szo = " "
while szo != "":
    szo = input("Egy szó: ")
    if szo != "":
        szavak.append(szo)

print(szavak)

legrovidebb = szavak[0]
leghosszabb = szavak[0]

for sz in szavak:
    if len(sz) > len(leghosszabb):
        leghosszabb = sz

    if len(sz) < len(legrovidebb):
        legrovidebb = sz
        
print("A leghosszabb szó:", leghosszabb)
print("A legrövidebb szó:", legrovidebb)
"""

# 1.
"""
szamok = [1, 54, 35, 67, 12]

for szam in szamok:
    if szam % 2 == 0:
        print("Az első páros szám: ", szam)
        break

for szam in szamok:
    if szam % 7 == 0:
        print("Az első héttel osztható szám: ", szam)
        break

for szam in szamok:
    if szam > 60 and szam < 70:
        print("Az első 60 és 70 közé eső szám: ", szam)
        break

index = 0
for szam in szamok:
    index += 1
    if szam == 12:
        print("12 indexe: ", index)
        break
"""

# 2.
"""
nevek = ['Elza', 'Melinda', 'Ferenc', 'Barbara', 'Vilma', 'Miklós', 'Ambrus', 'Mária', 'Natália', 'Judit', 'Árpád', 'Gabriella', 'Luca', 'Szilárda', 'Valér', 'Aletta', 'Lázár', 'Auguszta', 'Viola', 'Teofil', 'Tamás', 'Zénó', 'Viktória', 'Ádám', 'Eugénia', 'István', 'János', 'Kamilla', 'Tamara', 'Dávid', 'Szilveszter']
index = 0
for nev in nevek:
    index += 1
    if nev == "Teofil":
        print(index, "Teofil napja")
        break
"""

# 3., 4. - Nem tudom hogyan kell megoldani

#5.
"""
megallok = [450, 782, 1344, 1783, 1889, 2520, 2343, 1381, 1213]

index = 0
legmagasabb = megallok[0]
for i in range(len(megallok)):
    if megallok[i] > legmagasabb:
        legmagasabb = megallok[i]
        index = i

print(str(index) + ".", "megálló van a hegycsúcson.")
"""

# 7.
"""
nevek = ['Elza', 'Melinda', 'Ferenc', 'Barbara', 'Vilma', 'Miklós', 'Ambrus', 'Mária', 'Natália', 'Judit', 'Árpád', 'Gabriella', 'Luca', 'Szilárda', 'Valér', 'Aletta', 'Lázár', 'Auguszta', 'Viola', 'Teofil', 'Tamás', 'Zénó', 'Viktória', 'Ádám', 'Eugénia', 'István', 'János', 'Kamilla', 'Tamara', 'Dávid', 'Szilveszter']
nev = input("Vezetékneve: ")
index = 0
alkalmas = ""
for n in nevek:
    index += 1
    if n[0].lower() == nev[0].lower():
        alkalmas = n
        print("Az első alkalmas név a gyermekének:", n)
        print(index)
        break  
if alkalmas == "":
    print("Nics alkalmas névnap.")
"""

# 1.
"""
import random

szamok = []
for i in range(5):
    szamok.append(random.randint(1, 7))
szam = int(input("Egy szám: "))
for sz in szamok:
    if sz == szam:
        print("Benne volt a listában.")
        break

print(szamok)
"""

# 2
"""
szo = "alma"
betuk = []
betu = " "
while betu != "":
    betu = input("Egy betû: ")
    if betu != "":
        betuk.append(betu)
for i in szo:
    if i in betuk:
        print("Benne volt")
    print(i)
"""
