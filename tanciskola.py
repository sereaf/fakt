# fájlbeolvasása

tancok = []
tanc  = {}
adatok = []

with open("danceprogramme.txt") as fajl:
    for sor in fajl:
        adatok.append(sor.strip())
        if len(adatok) == 3:
            tanc["nev"] = adatok[0]
            tanc["lany"] = adatok[1]
            tanc["fiu"] = adatok[2]
            tancok.append(tanc)
            tanc = {}
            adatok = []
    print(tancok)

fajl.close()

print("2. Feladat")
print(f"Az elsőként bemutatott tánc neve: {tancok[0]['nev']}")
print(f"Az utolsóként bemutatott tánc neve: {tancok[-1]['nev']}")

print("3. Feladat")
szamlalo = 0
for tanc in tancok:
    if tanc["nev"] == "samba":
        szamlalo += 1

print(f"A sambát táncoló párok száma: {szamlalo}.")

print("4. Feladat")
print("Vilma az alábbi táncokban szerepelt:")
for tanc in tancok:
    if tanc["lany"] == "Vilma":
        print(tanc["nev"], end=" ")

print("5. Feladat")
bekert = input("Adjon meg egy táncot: ")
volt = False
for tanc in tancok:
    if tanc["lany"] == "Vilma" and tanc["nev"] == bekert:
        volt = True
        print(f"A  {bekert}  bemutatóján  Vilma  párja  {tanc['fiu']}  volt.")

if not volt:
    print(f"Vilma nem táncolt {bekert}-t.")

print("6. Feladat")

with open("szereplok.txt", "w") as szereplok:
    lanyok = set()
    fiuk = set()
    for tanc in tancok:
        fiuk.add(tanc["fiu"])
        lanyok.add(tanc["lany"])
    elvalaszto = ","
    print("Láynok:", elvalaszto.join(lanyok), file=szereplok)
    print("Fiúk:", elvalaszto.join(fiuk), file=szereplok)
    
print("a fájlba írás megtörtént")
