# 1
"""
bevetelek = []
bevetel = None
while bevetel != 0:
    bevetel = int(input("Bevétel: "))
    if bevetel != 0:
        bevetelek.append(bevetel)

ossz = 0
for i in bevetelek:
    ossz += i

print("Az összbevétel:", ossz)
"""

# 2
"""
ossz = 0
for i in range(7):
    ossz += float(input("Napi átlaghőmérséklet: "))
    
print("%.2f" % (ossz / 7))
"""

# 3
"""
szamok = [3.15, 5.9, 8.5, 8.9, 9.2, 14.0, 11.2, 28.2]
ossz = 0
for i in szamok:
    if i > 8:
        ossz += i

print("8-nál nagyobb számok összege:", ossz)
"""

# 4
"""
reszlanc = ["A", "G", "A", "A", "T", "A", "C", "T", "G", "A", "C", "T"]
ossz = 0
for i in reszlanc:
    if i == "G":
        ossz += 1

print(ossz, "Guanine bázis található a részláncban")
"""

# 5
"""
homeseklet = [-12, -8, 2, -2, -3, 4, 2, -2, 6, 3, 1, -5]
ossz = 0
for i in homeseklet:
    if i < 0:
        ossz += 1

print(ossz, "volt fagypont alat")
"""

# 6
"""
nevek = ["Erzsébet", "Jóska", "Antal", "Gábor", "Zoltán", "Katalin", "Mária", "Eszter"]
ossz = 0
for i in nevek:
    if i[0] == "E":
        ossz += 1

print(ossz, "kezdődik 'E' betűvel")
"""

# 7
"""
vizallasok = [8.3, 9.2, 9.3, 9.7, 10.3, 11.2, 11.8, 9.5, 8.3, 7.2]
for i in vizallasok:
    if i == 9.2:
        print("Volt 9.2 méteres mérés.")
        break
"""

# 8
"""
lottoszamok = [56, 10, 21, 87, 55]
ossz = 0
for i in lottoszamok:
    if i == 55:
        break
    ossz += 1
    
if ossz < 5:
    print("Benne volt az 55")
else:
    print("Nem volt benne az 55")
"""

# 9
"""
vizhozam = [45600, 97000, 32000, 25000, 62300, 42000]
ossz = 0
for i in vizhozam:
    if i > 40000:
        break
    ossz += 1
    
if ossz < len(vizhozam):
    print("Volt nagyobb 40000 liternél")
else:
    print("Nem volt nagyobb 40000 liternél")
"""

# 10
"""
bazisok = ["A", "G", "A", "A", "T", "A", "C", "T", "G", "A"]
ossz = 0
for i in bazisok:
    if i == "C":
        break
    ossz += 1
print(str(ossz) + ".", "helyen fordul először elő a C")
"""

# 11
"""
magassagok = [165, 175, 185, 190, 2]
legmagasabb = magassagok[0]
legmagasabb_tanulo = 0
legalacsonyabb = magassagok[0]
legalacsonyabb_tanulo = 0
for i in range(len(magassagok)):
    if magassagok[i] > legmagasabb:
        legmagasabb = magassagok[i]
        legmagasabb_tanulo = i
    if magassagok[i] < legalacsonyabb:
        legalacsonyabb = magassagok[i]
        legalacsonyabb_tanulo = i

print(str(legmagasabb_tanulo) + ".", "tanuló a legmagasabb: ", legmagasabb, "cm")
print(str(legalacsonyabb_tanulo) + ".", "tanuló a legalacsonyabb: ", legalacsonyabb, "cm")
"""
