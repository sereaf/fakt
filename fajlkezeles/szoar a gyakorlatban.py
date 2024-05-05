# szótár a gyakorlatban
# ADATOK BEOLVASÁSA

adatok = []
with open("diak_adatok.txt", "r", encoding="utf-8") as fajl:
    for sor in fajl:
        print(sor.strip())
        adatok.append(sor.strip())    
    
print(adatok)
fajl.close()

diak = {}
diakok = []
for elem in adatok:
    diak_adatai = elem.split()
    diak["vezeteknev"] = diak_adatai[0]
    diak["keresztnev"] = diak_adatai[1]
    diak["kor"] = int(diak_adatai[2])
    diak["osztaly"] = diak_adatai[3]
    if diak_adatai[4] == 1:
        diak["kollegista"] = True
    else:
        diak["kollegista"] = False
    diakok.append(diak)
    diak = {}
print(diakok)
print("2.Feladat")
print("10.A osztályos diákok: ")
for diak in diakok:
    if diak["osztaly"] == "10.A":
        print(diak["vezeteknev"] + " " + diak["keresztnev"])
# 3. Feladat Írjuk ki a diákok életkorának átlagát.
print("3. Feladat: ")
osz = 0
for diak in diakok:
    osz += diak["kor"]

atlag = osz / len(diakok)
print(f"A diákok átlagéletkora: {atlag:.2f}")

# 4. Feladat
print("4. Feladat")
osztaly_10B = [diak for diak in diakok if diak["osztaly"] == "10.B"]
print(osztaly_10B)
