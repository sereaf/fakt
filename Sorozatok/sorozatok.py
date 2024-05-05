# 1
print("1. Feladat")

sorozatok = []

with open("lista.txt") as f:
    a = []
    sorozat = {}
    for sor in f:
        s = sor.strip()
        a.append(s)
        if len(a) == 5:
            sorozat["datum"] = a[0]
            sorozat["sorozat"] = a[1]
            sorozat["resz"] = a[2]
            sorozat["hossz"] = a[3]
            sorozat["latta"] = True if a[4] == "1" else False
            sorozatok.append(sorozat)
            a = []
            sorozat = {}


# 2
print("2. Feladat")

osz = 0
for sorozat in sorozatok:
    if "NI" not in sorozat["datum"]:
        osz += 1
print(f"A listában {osz} db vetítési dátummal rendelkező epizód van. ")

# 3
print("3. Feladat")

latta = 0
for sorozat in sorozatok:
    if sorozat["latta"]:
        latta += 1
print(f"A listában lévő epizódok {(latta / (len(sorozatok)/100)):.2f}%-át látta. ")

# 4
print("4. Feladat")

ossz = 0
for sorozat in sorozatok:
    if sorozat["latta"]:
        ossz += int(sorozat["hossz"])
nap = ossz // (60 * 24)
ora = ossz % (60 * 24) //  60
perc = ossz % 60

print(f"Sorozatnézéssel {nap} napot {ora} órát és {perc} percet töltött.")

# 5
print("5. Feladat")

datum = input("Datum: ")

for s in sorozatok:
    if s["datum"] <= datum and s["latta"]:
        print(s["resz"] + '\t' + s["sorozat"])
