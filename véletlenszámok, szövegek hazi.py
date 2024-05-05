# 1.
'''
print("*" * 10)
'''

# 2.
'''
for i in range(0, 5):
    print("*")
'''

# 3.
'''
for i in range(1, 6):
    print("*" * i)
'''

# 1.
'''
for i in range(2, 11, 2):
    print(i)
'''

# 2. 
'''
for i in range(10, 0, -1):
    print(i)
'''

# 3.
'''
for i in range(9, 0, -2):
    print(i)
'''

# 4. 
'''
szoveg = input("Szöveg: ")
ennyiszer = int(input("Írja ki ennyiszer: "))

for i in range(0, ennyiszer):
    print(szoveg)
'''

# 5.
'''
szam = 1
while szam % 2 != 0:
    szam = int(input("Páros szám: "))
'''

# 6.
'''
import random

for i in range(0, 20):
    szam = random.randint(1, 12)
    if szam % 3 == 0:
        print(szam)
'''

# 1.
'''
szam = int(input("Páros szám: "))

for i in range(0, szam):
    if i < (szam / 2):
        print("O" * (i + 1))
    else:
        print("O" * (szam - i))
'''

# 2.
'''
for i in range(0, 5):
    sor = ""
    for a in range(0, 5):
        if a == i:
            sor = sor + "O"
        else:
            sor = sor + "."
    print(sor)
'''

# 3.

for i in range(0, 7):
    sor = ""
    for a in range(0, 7):
        if a == i or a == 6 - i:
            sor = sor + "O"
        else:
            sor = sor + "."
    print(sor)

