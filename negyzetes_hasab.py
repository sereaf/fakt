a = float(input("A négyzetes hasáb a oldala centiméterben: "))
b = float(input("A négyzetes hasáb b oldala centiméterben: "))

A = 2 * (a**2) + (4 * a * b)
V = (a**2) * b


print("A négyzetes hasáb felszíne: ", "%.2f"%A, "cm2", sep="")
print("A négyzetes hasáb térfogata: ", "%.2f"%V, "cm3", sep="")
