from math import *


a = float(input("A derékszögű háromszög a oldala centiméterben: "))
b = float(input("A derékszögű háromszög b oldala centiméterben: "))

c = sqrt((a**2) + (b**2))

print("A derékszögű háromszög harmadik oldala: ", "%.2f"%c, "cm", sep="")
