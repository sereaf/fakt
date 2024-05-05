# 1
print("1. Feladat")

sz = int(input("Melyik számot? "))
osz = 2
while sz > 1:
    if sz % osz == 0:
        print(sz, "|", osz)
        sz = sz // osz
    else:
        osz = osz + 1
print(1, "|")

# 2
print("2. Feladat")

tavolsagok = [float(i) for i in input("Távolságok: ").split(", ")]
eddig = 0
for t in tavolsagok:
    eddig += t
    if eddig > 150:
        print("szünet")
        eddig = t
    print(t, "km")
