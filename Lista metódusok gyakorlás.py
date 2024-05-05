# 1.1, 1.2, 1.3
'''
szin = input("Szín: ")

szinek = ["kék", "zöld", "piros", "sárga"]

if szinek.count(szin) != 0:
    print("Ennyiszer volt benne: ", szinek.count(szin))
else:
    print("Még nem volt benne")

szinek.append(szin)
print(szinek)
'''

# 2.

import random

szam = int(input("Szám: "))

szamok = []

for i in range(10):
    szamok.append(random.randint(1, 3))

print(szamok)

if szam in szamok:
    szamok.remove(szam)

print(szamok)
