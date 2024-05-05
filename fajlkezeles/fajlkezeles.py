"""
# beolvasás soronként
lista = []
forasfajl = open("diak_adatok.txt")
for sor in forasfajl:
    lista.append(sor.strip())
forasfajl.close()
print(lista)

# beolvasás egyben
file = open("diak_adatok.txt")
lista1 = file.readlines()
lista_vegeknelkul = []
for elem in lista1:
    lista_vegeknelkul.append(elem.strip())
file.close()
print(lista1)
print(lista_vegeknelkul)
"""

# íras fájlba
lista2 = ["Opel", "Ford", "Toyota"]
celfajl = open("auto.txt", "w")
for elem in lista2:
    print(elem, file=celfajl)
celfajl.close()
print("A fájlba írás megtörtént")
