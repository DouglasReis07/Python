import math
an = float(input("Digite um angulo: "))
seno = math.sin(math.radians(an))
print(f"O ângulo de {an} tem o SENO de {seno:.2f}")
cosseno = math.cos(math.radians(an))
print(f"O ângulo de {an} tem o cosseno de {cosseno:.2f}")
tangente = math.tan(math.radians(an))
print(f"O ângulo de {an} tem a tangente de {tangente:.2f}")