# 1.

jegyek = input("jegyek: ")

l = jegyek.split()

ossz = 0
for i in l:
    ossz += int(i)
print(f"Átlag: {ossz/len(l)}")

legk = int(l[0])
for i in l:
    if int(i) < legk:
        legk = int(i)
print(f"Amanda leggyengébb érdemjegye a tárgyból: {legk}")

if l.count("5") >= 1:
    print("Volt ötöse")
else:
    print("Nem volt ötöse")

print(f"{l.count(str(legk))} leggyengébb érdemjegye volt")

hany = 1
for i in l:
    if int(i) == legk:
        print(f"{hany}. volt az elsõ leggyengébb jegye")
        break
    else:
        hany += 1
        
volte = False
hany = 1
for i in l:
    if int(i) == 3:
        print(f"{hany}. volt az elsõ közepes jegye")
        volte = True
        break
    else:
        hany += 1

if not volte:
    print("Nem volt közepes jegye.")


# 2

import math

szama = input("tyúktojások száma: ")
szama = szama.split()

for i in szama:
    if int(i) < 30:
        szama = input("tyúktojások száma: ")
        break

ossz1 = 0
adozok = 0
legk = math.floor((int(szama[0])/100)*10)
volte = False
for i, a in enumerate(szama):
    ado = math.floor((int(a)/100)*10)
    print(f"Adó: {ado}")
    if ado <= legk:
        legk = ado
        legki = i + 1
    if ado >= 5:
        adozok += 1
    elif ado >= 10:
        volte = True
    ossz1 += ado

ossz2 = 0
for i in szama:
   ossz2 += int(i) 

print(f"{ossz2-ossz1} tojás marad összesen")

print(f"{adozok} telek adózott legalább öt tojást")

print(f"{legki}. telek adózta a legkevesebbet, ami {legk} volt")

if volte:
    print("Volt olyan akki tíz, vagy annál is több tojást adózott")
else:
    print("Nem volt olyan akki tíz, vagy annál is több tojást adózott")
