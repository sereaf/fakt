# ciklus számlálós

'''
for i in range(10):
    print(i, end=' ')
'''
'''

for i in range(2, 11, 2):
    print(i, end=' ')
'''
'''

for i in range(10, 0, -1):
    print(i, end=' ')
'''

# egymásba ágyazott ciklusok

'''
# szorzótábla írása
n = 3 # ciklust 3* szeretnénk futattni
for a in range(1, n+1):
    for b in range(1, n+1):
        print(b, "*", a, '=', b * a)

'''

# feltételes ciklus - while

'''
# kör kerületének számítása végjelig
from math import *

r = 10

while r != 0: # addig ismételünk, amíg r nem lesz 0
    r = float(input("Kör sugara: "))
    k = 2 * r * pi
    if r != 0:
        print('A kör kerülete: ', '%.2f'%k)
'''

tabla = 7 # 7 es szorzótábla kikérdezése
passzok = 0
jo_valaszok = 0
rossz_valaszok = 0

for i in range(1, 11):
    print("Mennyi ", i, "*", tabla, "?", sep="", end=" ")
    tipp = input()
    if tipp == "stop":
        break
    if tipp == "passz":
        print("Kihagyva")
        passzok += 1
        continue
    megoldas = i*tabla
    if (int(tipp) == megoldas):
        jo_valaszok += 1
        print("Helyes")
    else:
        rossz_valaszok += 1
        print("Nem jó! Helyes válasz: ", megoldas)
print("Vége a feladatnak")
print(passzok)
