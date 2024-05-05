# 1.1, 1.2
"""
import random

szamok = []
osszesen = 0
for i in range(5):
    szam = random.randint(0, 10)
    szamok.append(szam)
    if szam % 2 == 0:
        osszesen += szam

print(osszesen)
print(szamok)
"""

# 2.
"""
szamok = []
osszesen = 0
szam = 0
while szam >= -5 and szam <= 5:
    szam = int(input("Egész szám [-5;5] intervallumban: "))
    if szam >= -5 and szam <= 5:
        osszesen += szam
        szamok.append(szam)
print(szamok)
print(osszesen)
"""

# 3.
"""
ar = int(input("Ár: "))

valtozasok = [12, 3, -4, 8, 9]

for i in valtozasok:
    ar = (ar / 100) * (100 + i)

print("Az új ár: ", ar)
"""
# 4
"""
szam = 1
osszeg = 0
while szam <= 100:
    osszeg += szam
    szam += 1

print(osszeg)
"""

# 5
meccsek = ["ny", "ny", "v", "d", "d", "d", "v", "v", "ny", "ny", "d"]
pontok = 0
for i in meccsek:
    if i == "ny":
        pontok += 3
    elif i == "d":
        pontok += 1
print("Pontok: ", pontok)
