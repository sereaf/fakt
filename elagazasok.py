# 1.1, 1.2 Feladat

'''
valasz = input("Jó napja van? ")

if valasz == "igen":
    print("Jó napja van")
elif valasz == "nem":
    print("Rossz napja van")
else:
    print("Sajnos nem értem a válaszodat!")
'''

# 2. Feladat

'''
szam = int(input("Szám: "))

if szam % 2 == 0:
    print("Páros")
else:
    print("Páratlan")
'''


# 3. Feladat

'''
import random

szam1 = random.randint(0, 5)

szam2 = int(input("Szám: "))


if szam2 > szam1:
    print("A te számod nagyobb")
elif szam2 < szam1:
    print("A te számod kisebb")
else:
    print("Egyenlő")

'''

# 1. Feladat

'''
szam = int(input("Szám: "))

if szam > 0 and szam % 2 == 0:
    print("pozitív páros")
elif szam < 0 and szam % 2!= 0:
    print("negatív páratlan")
else:
    print("egyik sem")
'''


# 2. Feldat

'''
henrik = input("Jön Henrik ma kosarazni? ")
hanna = input("Jön Hanna ma kosarazni? ")

if henrik == "nem" and hanna == "nem":
    print("egyikük sem jön kosarazni")
elif henrik == "igen" and hanna == "igen":
    print("mind a ketten jönnek kosarazni")
else:
    print("csak az egyikük jön kosarazni")

'''

# 3.Feladat

'''
szam = int(input("Szám: "))

harommal = szam % 3 == 0
neggyel = szam % 4 == 0

if harommal and neggyel:
    print("3-mal és 4-gyel is osztható")
elif not harommal and not neggyel:
    print("sem 3-mal, sem 4-gyel nem osztható")
elif harommal and not neggyel:
    print("csak 3-mal osztható")
elif not harommal and neggyel:
    print("csak 4-gyel osztható")
'''

# 1. Feladat

'''
import random

szam1 = random.randint(1, 3)
szam2 = int(input("Szám: "))

if szam1 == szam2:
    print("egyenlõ")
else:
    print("nem egyenlõ")

'''

# 2. Feladat

import random

szam = random.randint(1, 2)

fej_vagy_iras = input("Fej vagy írás: ")

if fej_vagy_iras == "fej" and szam == 1 or fej_vagy_iras == "írás" and szam == 2:
    print("Eltaláltad")
else:
    print("Nem találtad el")

