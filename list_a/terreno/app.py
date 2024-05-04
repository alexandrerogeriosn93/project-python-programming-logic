width = float(input("Digite a largura do terreno: "))
length = float(input("Digite o comprimento do terreno: "))
value = float(input("Digite o valor do metro quadrado: "))

area = width * length
price = area * value

print(f"Área do terreno = {area:.2f}\nPreço do terreno = {price:.2f}")
