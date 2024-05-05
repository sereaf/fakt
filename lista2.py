# 1.
"""
lovak = ["Ráró", "Baró", "Tipró", "Karó"]
szinek = []

for i in lovak:
    szinek.append(input(i + " színe: ")) 
"""

# 2.
"""
allat_neve = " "
allatok_neve = []
while allat_neve != "":
    allat_neve = input("Állat neve: ")
    if allat_neve != "":
        allatok_neve.append(allat_neve)

kajak = []
for i in allatok_neve:
    kajak.append(input(i+ " kajája: "))
"""

# 3.
"""
szavak = []
for i in range(10):
    szavak.append(input("Szó: "))

for i in szavak:
    print((i + " ") * 9 + i + ".")
"""

# 4.
"""
szavak = []
for i in range(10):
    szavak.append(input("Szó: "))

for i in range(5):
    for a in range(9):
        print(szavak[a], end=' ')
    print(szavak[-1] ,end='')
    print('.')
"""


# 1.
"""
kiralysagok = []
nagyhercegsegek = []
hercegsegek = []

kiralysag = " "
while kiralysag != "":
    print(kiralysagok)
    kiralysag = input("Egy európai királyság: ")
    if kiralysag != "":
        kiralysagok.append(kiralysag)

nagyhercegseg = " "
while nagyhercegseg != "":
    print(nagyhercegsegek)
    nagyhercegseg = input("Egy európai nagyhercegség: ")
    if nagyhercegseg != "":
        nagyhercegsegek.append(nagyhercegseg)

hercegseg = " "
while hercegseg != "":
    print(hercegsegek)
    hercegseg = input("Egy európai hercegség: ")
    if hercegseg != "":
        hercegsegek.append(hercegseg)
    
monarchiak = kiralysagok + nagyhercegsegek + hercegsegek
monarchiak.append("Vatikán")
print(monarchiak)
"""

# 2.

import random

dobasok = []
for i in range(10000000):
    dobasok.append(random.randint(1, 6))

print("1: ", dobasok.count(1))
print("2: ", dobasok.count(2))
print("3: ", dobasok.count(3))
print("4: ", dobasok.count(4))
print("5: ", dobasok.count(5))
print("6: ", dobasok.count(6))
