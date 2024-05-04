from math import pow

a, b, c = [float(x) for x in input("Digite as medidas A, B e C: ").split(" ")]

square_area = pow(a, 2)
triangle_area = (a * b)/2
trapeze_area = ((a + b) * c)/2 

print(f"Area do quadrado = {square_area:.4f}\nArea do trianguo = {triangle_area:.4f}\nArea do trapezio = {trapeze_area:.4f}")
