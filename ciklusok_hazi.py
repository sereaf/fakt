# 1., 2. Feladat

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
        passzok = passzok + 1
        continue
    megoldas = i*tabla
    if (int(tipp) == megoldas):
        jo_valaszok = jo_valaszok + 1
        print("Helyes")
    else:
        rossz_valaszok = rossz_valaszok + 1
        print("Nem jó! Helyes válasz: ", megoldas)
print("Vége a feladatnak")

print("Passzok: ", passzok, "Jó válaszok: ", jo_valaszok, "Rossz Válaszok: ", rossz_valaszok)

if jo_valaszok == 10:
    print("Ügyes")
elif rossz_valaszok > 1:
    print("Gyakorolj")

if passzok > 0:
    print("Ne passzolj!!!")
'''

# 3. Feladat

'''
jelszo = "jelszo"
for i in range(0, 3):
    tipp = input("Jelszó: ")
    if tipp == jelszo:
        print("bemehet")
        break
    else:
        print("hozzáférés  megtagadva")
'''

# 4. Feladat

'''
for i in range(1, 101):
    print(i**2)
'''

# 5. Feladat

'''
for i in range(0, 100, 2):
    print(i)
'''

# 6. Feladat

'''
for i in range(101, 1000, 2):
    print(i)
'''

# 7., 8. Feladat

ettol = int(input("Ettõl: "))
eddig = int(input("Eddig: "))
ennyivel = int(input("Ennyivel: "))


for i in range(ettol, eddig + 1, ennyivel):
    print(i)


