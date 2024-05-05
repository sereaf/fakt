# 1, 2

"""
forasfajl = open("fajlkezeles.txt")
for sor in forasfajl:
    print(sor)
forasfajl.close()
"""
# 3
"""
lista = []
forasfajl = open("fajlkezeles.txt")
for sor in forasfajl:
    lista.append(sor.strip())
forasfajl.close()
print(lista)
"""
# 4
"""
forasfajl = open("fajlkezeles.txt")
celfajl = open("celfajl.txt", "w")
for sor in forasfajl:
    print(sor, file=celfajl)
forasfajl.close()
celfajl.close()
"""

# 5
"""
lista = []
forasfajl = open("fajlkezeles.txt")
celfajl = open("celfajl.txt", "w")
for sor in forasfajl:
    lista.append(sor.strip())
forasfajl.close()

for elem in lista:
    print(elem, file=celfajl)
celfajl.close()
"""

# 6
"""
forasfajl = open("fajlkezeles.txt")
celfajl = open("celfajl.txt", "w")
for sor in forasfajl:
    print(sor, file=celfajl)
forasfajl.close()
celfajl.close()
"""

# 7
"""
lista = []
forasfajl = open("fajlkezeles.txt")
celfajl = open("celfajl.txt", "w")
for sor in forasfajl:
    lista.append(sor)
forasfajl.close()

szoveg = ""
for elem in lista:
    szoveg = elem + szoveg

print(szoveg)
print(szoveg, file=celfajl)
celfajl.close()
"""

# 8

"""
lista = []
forasfajl = open("fajlkezeles.txt")
for sor in forasfajl:
    lista.append(sor)
forasfajl.close()

ossz = 0
szoveg = "" 
for elem in lista:
    sor = ""
    for kar in elem:
        if kar == "e" or kar == "E":
            ossz += 1
            sor += "*"
        else:
            sor += kar
    szoveg += sor
print(szoveg)
print("Összesen", ossz, "betűt helyettesített csillaggal.")
"""
