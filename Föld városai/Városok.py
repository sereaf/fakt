# 1

varosok = []
with open("varosok.csv",encoding="utf-8") as f:
    elso_sor = False
    for sor in f:
        if elso_sor:
            varos = {}
            s = sor.strip().split(";")
            varos["varos"] = s[0]
            varos["orszag"] = s[1]
            varos["nepesseg"] = int(s[2].split(",")[0]+s[2].split(",")[1])
            varosok.append(varos)
        elso_sor = True

# 2

print("2. Feladat")

print(f"Városok száma: {len(varosok)}")

# 3
print("3. Feladat")

ossz = 0
for varos in varosok:
    if varos["orszag"] == "India":
        ossz += varos["nepesseg"]

print(f"Az indiai nagyvárosok lakosságának összege: {ossz} fõ")

# 4
print("4. Feladat")

legnagyobb_varos = varosok[0]
for varos in varosok:
    if varos["nepesseg"] > legnagyobb_varos["nepesseg"]:
        legnagyobb_varos = varos    

print("A legnagyobb város adatai: ")
print(f"\tNév: {legnagyobb_varos['varos']}")
print(f"\tOrszág: {legnagyobb_varos['orszag']}")
print(f"\tLakosság: {legnagyobb_varos['nepesseg']}")

# 5
print("5. Feladat")

van = False
for varos in varosok:
    if varos["orszag"] == "Magyarország":
        print("Van magyar varos az adatok között.")
        van = True
        break

if not van:
    print("Nincs magyar varos az adatok között.")

# 6
print("6. Feladat")

ossz = 0
for varos in varosok:
    if len(varos["varos"].split()) == 2:
        ossz += 1
print(f"Városok egy szóközzel: {ossz}")


# 7
print("7. Feladat")

ossz_varos = []
for varos in varosok:
    ossz_varos.append(varos["orszag"])
var = set(ossz_varos)
for v in var:
    print(f"\t{v}: {ossz_varos.count(v)} db")

# 8
print("8. Feladat")

with open("kina.txt", "w") as f:
    for varos in varosok:
        if varos["orszag"] == "Kína":
            print(f"{varos['varos']};{varos['nepesseg']}", file=f)
