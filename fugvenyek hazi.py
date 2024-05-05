# Eljárásos feladatok

# 1.
'''
def alakzat():
    print("Alakzat: ")
    for i in range(1, 6):
        print(" " * (i-1), "O")

alakzat()
'''

# 2.
'''
def negativ_v_pozitiv(szam):
    if szam > 0:
        print("Pozitív")
    elif szam != 0:
        print("Negatív")
    else:
        print("Nulla")
'''

# 3.
'''
def nagyobb_v_kisebb(szam1, szam2):
    if szam1 > szam2:
        print("Az első szám nagyobb")
    elif szam1 == szam2:
        print("Egyenlőek")
    else:
        print("Az második szám nagyobb")
'''

# 4.
'''
szo1 = input("Az első szó: ")
szo2 = input("Az második szó: ")
szo3 = input("Az harmadik szó: ")

szavak = [szo1, szo2, szo3]

def legrovidebb_szo(szavak):
    legrovidebb = 0
    hossz = len(szavak[0])
    for i in range(len(szavak)):
        if len(szavak[i]) < hossz:
            hoszz = len(szavak[i])
            legrovidebb = i
    print("A legrövidebb szó:", szavak[legrovidebb])

legrovidebb_szo(szavak)
'''


# 5.
'''
def mezot_rajzol(x, y):
    for i in range(3):
        sor = ""
        for a in range(6):
            if a == x and i == y:
                sor += "+"
            else:
                sor += "O"
        print(sor)

x = 1
y = 1
while x >= 0 and y >= 0:
    x = int(input("x: "))
    y = int(input("y: "))
    mezot_rajzol(x, y)
'''

# Függvényes feladatok

# 1.
'''
def osszegzo(szamok):
    osszeg = 0
    for i in range(len(szamok)):
        osszeg += szamok[i]
    return osszeg

osszegzo([1, 2, 3])
'''

# 2.
'''
def paros_e(szamok):
    for i in range(len(szamok)):
        if szamok[i] % 2 == 0:
            return True
    return False
    
paros_e([1, 2, 3])
'''

# 3.
'''
def harommal_oszthatok(szamok):
    osszeg = 0
    for i in range(len(szamok)):
        if szamok[i] % 3 == 0:
            osszeg += 1
    return osszeg

szamok = []
szam = 0
while szam >= 0:
    szam = int(input("Szám: "))
    if szam >= 0:
        szamok.append(szam)

harommal_oszthatok(szamok)
'''

# 4.

# 5.

def legkisebb(szamok):
    legkisebb = szamok[0]
    for i in range(len(szamok)):
        if szamok[i] < legkisebb:
            legkisebb = szamok[i]
    return legkisebb

szamok = []
szam = 0
while szam >= 0:
    szam = int(input("Szám: "))
    if szam >= 0:
        szamok.append(szam)

print("A legkisebb szám:", legkisebb(szamok))

    
