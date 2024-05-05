# 1

zenek = []
def beolvas():
    fajl = open("playlist.csv")
    zene = {}
    for sor in fajl:
        adatok = sor.strip().split(";")
        zene["eloado"] = adatok[0]
        zene["cim"] = adatok[1]
        zene["mufaj"] = adatok[2]
        zene["hossz"] = int(adatok[3])
        zenek.append(zene)
        zene = {}

    fajl.close()

beolvas()
print(zenek)


# 2

def teljes_hossz(lista):
    ossz = 0
    for zene in lista:
        ossz += zene["hossz"]
    perc = int(ossz / 60)
    masodperc = ossz % 60
    celfajl = open("02_hossz.txt", "w")
    print(f"A lejatszasi lista hossza: {perc} perc, {masodperc} masodperc", file=celfajl)
    celfajl.close()
teljes_hossz(zenek)

# 3

def leghosszabb_rockzene(lista):
    leghosszabb = 0
    cim = ""
    for zene in lista:
        if zene["mufaj"] == "rock" and zene["hossz"] > leghosszabb:
            leghosszabb = zene["hossz"]
            cim = zene["cim"]
    celfajl = open("03_leghosszabb_rock.txt", "w")
    print(cim, file=celfajl)
    celfajl.close()
leghosszabb_rockzene(zenek)

# 4

def leggyakoribb_mufaj(lista):
    rock = 0
    pop = 0
    metal = 0
    for zene in lista:
        if zene["mufaj"] == "rock":
            rock += 1
        elif zene["mufaj"] == "pop":
            pop += 1
        elif zene["mufaj"] == "metal":
            metal += 1
    celfajl = open("04_kedvenc_mufaj.txt", "w")
    if pop > rock and pop > metal:
        print("POP", file=celfajl)
    elif rock > pop and rock > metal:
        print("ROCK", file=celfajl)
    else:
        print("METAL", file=celfajl)
    celfajl.close()
    
leggyakoribb_mufaj(zenek)
