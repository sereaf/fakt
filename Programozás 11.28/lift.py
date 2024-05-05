# 1
print("1. Feladat")

igenyek = []
with open("igeny.txt") as f:
    for i, s in enumerate(f):
        igeny = {}
        if i == 0:
            szintek = int(s)
        elif i == 1:
            csapatok = int(s)
        elif i== 2:
            igenyek_szama = int(s)
        else:
            s = s.strip().split()
            igeny["ora"] = int(s[0])
            igeny["perc"] = int(s[1])
            igeny["mperc"] = int(s[2])
            igeny["sorszam"] = int(s[3])
            igeny["indulo"] = int(s[4])
            igeny["cel"] = int(s[5])
            igenyek.append(igeny)


# 2
print("2. Feladat")

kezd = int(input("Melyik szinten áll a lift? "))

# 3
print("3. Feladat")

print(f"A lift a {igenyek[-1]['cel']}. szinten áll az utolsó igény teljesítése után.")

# 4
print("4. Feladat")

legalacs = kezd
legmag = kezd
for i in igenyek:
    if i["indulo"] < legalacs :
        legalacs = i["indulo"]
    elif i["cel"] < legalacs:
        legalacs = i["cel"]

    if i["indulo"] > legmag :
        legmag = i["indulo"]
    elif i["cel"] > legmag:
        legmag = i["cel"]
print(f"A megfigyelés kezdete és az utolsó igény teljesítése közötti legalacsonyabb: {legalacs} és legmagasabb: {legmag}")


# 5
print("5. Feladat")

utassal = 0
for i in igenyek:
    if i["cel"] > i["indulo"]:
        utassal += 1

utasn = 0
for i in range(len(igenyek)):
    if i < len(igenyek)-1:
        if igenyek[i+1]["indulo"] > igenyek[i]["cel"]:
            utasn += 1

print(f"Utassal: {utassal}, utas nélkül: {utasn}")

# 6
print("6. Feladat")

sorszamok = []
for a in igenyek:
    sorszamok.append(a["sorszam"])

for i in range(csapatok+1):
    if i not in sorszamok and i != 0:
        print(i, end=" ")

# 7
print()
print("7. Feladat")

import random

csapat = random.randint(1, csapatok)
ig = []
for i in igenyek:
    if i["sorszam"] == csapat:
        ig.append(i)
erkezett = ig[0]["cel"]
vetett = False
for i, a in enumerate(ig):
    if i != 0:
        if a["indulo"] != erkezett:
            vetett = True
            print(f"A {csapat}. csapat {erkezett} és {a['indulo']} szintek között vétett  a  szabályok  ellen!")
            break
        else:
            erkezett = a["cel"]
if not vetett:
    print("Nem bizonyítható szabálytalanság")


# 8
print("8. Feladat")

