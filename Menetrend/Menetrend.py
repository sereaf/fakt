# 1
print("1. Feladat")

utak = []

with open("vonat.txt") as f: 
    for sor in f:
        ut = {}
        s = sor.strip().split()
        ut["vonat"] = s[0]
        ut["allomas"] = s[1]
        ut["ora"] = s[2]
        ut["perc"] = s[3]
        ut["indul"] = True if s[4] == "I" else False
        utak.append(ut)

# 2
print("2. Feladat")

vonatok = []
allomasok = []
for ut in utak:
    vonatok.append(ut["vonat"])
    allomasok.append(ut["allomas"])
    
vonatok = set(vonatok)
allomasok = set(allomasok)

print(f"Az állomások száma: {len(allomasok)}")
print(f"A vonatok száma: {len(vonatok)}")

# 3
print("3. Feladat")

legtobb = 0

for ut in utak:
    if ut["indul"] == False:
        for u in utak:
            if u["vonat"] == ut["vonat"] and u["allomas"] == ut["allomas"] and u["indul"]:
                indulas = int(ut["ora"]) * 60 + int(ut["perc"])
                erkezes = int(u["ora"]) * 60 + int(u["perc"])
                if erkezes - indulas > legtobb:
                    legtobb = erkezes - indulas
                    legtobb_allomas = ut["allomas"]
                    legtobb_vonat = ut["vonat"]
print(f"A(z) {legtobb_vonat}. vonat a(z) {legtobb_allomas}. állomáson {legtobb} percet állt.")


# 4
print("4.Feladat")

azonosito = input("Adja meg egy vonat azonosítóját! ")
ido = input("Adjon meg egy időpontot (óra perc)!  ")


# 5

print("5.Feladat")

eloirt = 2 * 60 + 22
vizsgalt_indulas = 0
vizsgalt_erkezes = 0

for ut in utak:
    if int(utak["allmas"]) == 0 and ut["vonat"] == azonosito:
        vizsgalt_indulas = int(ut["ido"]) * 60 + int(ut["perc"])
    if ut["allomas"] == len(allomasok)-1 and ut["vonat"] == azonosito:
        vizsgalt_erkezes = int(ut["ido"]) * 60 + int(ut["perc"])
elteres = eloirt - (vizsgalt_erkezes - vizsgalt_indulas)
print(elteres)


# 6
print("6.Feladat")
with open(f"halad{azonosito}.txt", "w") as f:
    for ut in utak:
        if ut["vonat"] == azonosito and ut["indul"] == False:
            print(f"{ut['allomas']}. állomás {ut['ora']}:{ut['perc']}", file=f)

