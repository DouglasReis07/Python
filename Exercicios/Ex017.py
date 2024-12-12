import math
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
h1 = math.hypot(co, ca)
print(f"A hipotenusa vai medir {h1:.2f}")