# 1
print("1. Feladat")

fogadoorak = []
with open("fogado.txt") as f:
    for sor in f:
        ora={}
        o = sor.strip().split()
        ora["nev"] = o[0] + " " + o[1]
        ora["foglalas"] = o[2]
        ora["lefoglalas"] = o[3]
        fogadoorak.append(ora)

# 2
print("2. Feladat")

ossz = 0
for ora in fogadoorak:
    ossz += 1
print(f"Foglalások száma: {ossz}")

# 3
print("3. Feladat")

nev = input("Egy tanár neve: ")

ossz = 0
for ora in fogadoorak:
    if ora["nev"] == nev:
        ossz += 1

if ossz == 0:
    print("A megadott néven nincs időpontfoglalás")
else:
    print(f"A megadott néven {ossz} időpontfoglalás van")

# 4
print("4. Feladat")

idopont = input("Egy időpont: ")

tanarok = []
for ora in fogadoorak:
    if ora["foglalas"] == idopont:
        tanarok.append(ora["nev"])
tanarok.sort()
for tanar in tanarok:
    print(tanar)

with open(f"{idopont.split(':')[0]+idopont.split(':')[1]}.txt", "w") as f:
    for tanar in tanarok:
        print(tanar, file=f)
        
# 5
print("5. feladat")

index = 0
legkorabb = fogadoorak[0]["lefoglalas"]
for i, ora in enumerate(fogadoorak):
    if ora["lefoglalas"] < legkorabb:
        legkorabb = ora["lefoglalas"]
        index = i

print(f"Tanar neve:", fogadoorak[index]["nev"])
print(f"Foglalt időpont:", fogadoorak[index]["foglalas"])
print(f"Foglalás ideje:", fogadoorak[index]["lefoglalas"])

# 6
print("6. feladat")

idopontok = []
for i in range(6):
    idopontok.append(f"16:{i}0")
    idopontok.append(f"17:{i}0")

foglalt_idopontok = []
for ora in fogadoorak:
    if ora["nev"] == "Barna Eszter":
        foglalt_idopontok.append(ora["foglalas"])
for idopont in idopontok:
    if idopont not in foglalt_idopontok:
        print(idopont)

legkorabb = idopontok[0]
for idopont in foglalt_idopontok:
    if idopont > legkorabb:
        legkorabb = idopont
for idopont in idopontok:
    if idopont > legkorabb:
        legkorabb = idopont
        break
print(f"Barna Eszter legkorábban távozhat: {legkorabb}")
