from math import pow, sqrt

def calc_delta(a, b, c):
    return pow(b, 2) - (4 * a * c)

def calc_x1(a, b, delta):
    return (-b + sqrt(delta))/(2 * a)

def calc_x2(a, b, delta):
    return (-b - sqrt(delta))/(2 * a)

a, b, c = [float(x) for x in input("Digite os coeficientes A, B e C: ").split(" ")]

delta = calc_delta(a, b, c)

if(a == 0 or delta < 0):
    print("Esta equacao nao possui raizes reais")
else:
    x1 = calc_x1(a, b, delta)
    x2 = calc_x2(a, b, delta)
    print(f"X1 = {x1:.4f}\nX2 = {x2:.4f}")
