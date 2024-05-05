# 1.
"""
helyezes = int(input("Hányadik lett a versenyen? "))

if helyezes == 1:
    print("Arany érem.")
elif helyezes == 2:
    print("Ezüst érem")
elif helyezes == 3:
    print("Bronz érem")
"""

# 2.
'''
marha = input("Van benne marha? (igen/nem) ")
pulyka = input("Van benne pulyka? ")
sonka = input("Van benne sonka? ")
sajt = input("Van benne sajt? ")

if marha == "igen" or pulyka == "igen" or sonka == "igen":
    if (marha == "igen" and sonka == "igen") == False:
        if pulyka == "igen":
            if sajt == "igen":
                print("Jó")
            else:
                print("Rossz")
        else:
            print("Jó")
    else:
        print("Rossz")
else:
    print("Rossz")
'''
# 2.b
'''
szegfűbors = input("Van benne szegfűbors? (igen/nem) ")
szerecsendió  = input("Van benne szerecsendió ? ")
fahéj = input("Van benne fahéj? ")

if (szegfűbors == "igen" and szerecsendió == "igen") == False:
    if fahéj == "igen":
        if szerecsendió == "igen":
            print("Jó")
        else:
            print("Rossz")
    else:
        if szerecsendió == "igen":
            print("Rossz")
        else:
         print("Jó")
else:
    print("Rossz")
'''
# 2.c
"""
olívabogyó = input("Van benne olívabogyó? (igen/nem) ")
pepperoni = input("Van benne pepperoni  ? ")
sonka = input("Van benne sonka? ")

if pepperoni == "igen":
    if olívabogyó == "igen":
        print("Jó")
    else:
        print("Rossz")
else:
    print("Rossz")
"""

# 3., 4. - Nem tudom hogyan kell megoldani

# 5.

eloadok = []
cimek = []
for i in range(5):
    eloado = input("Kedvenc zenei előadója neve: ")
    cim = input("Kedvenc szám címe: ")
    eloadok.append(eloado)
    cimek.append(cim)
