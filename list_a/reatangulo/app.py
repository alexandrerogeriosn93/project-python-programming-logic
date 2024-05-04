from math import sqrt, pow

base = float(input("Base do retângulo: "))
height = float(input("Altura do retângulo: "))

area = base * height
perimeter = (base * 2) + (height * 2)
diagonal = sqrt(pow(height, 2) + pow(base, 2))

print(f"Área = {area:.4f}\nPerímetro = {perimeter:.4f}\nDiagonal = {diagonal:.4f}")
