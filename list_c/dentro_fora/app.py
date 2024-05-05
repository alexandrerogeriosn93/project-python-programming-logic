def check_interval(num):
    return num >= 10 and num <= 20

n = int(input("Quantos numeros voce vai digitar? "))

inside, out = 0, 0

for i in range(n):
    x = int(input("Digite um numero: "))

    if check_interval(x):
        inside += 1
    else:
        out += 1

print(f"{inside} Dentro\n{out} Fora")
