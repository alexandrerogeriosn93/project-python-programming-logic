def check_is_null(num):
    return num == 0

def check_positive(num):
    return num > 0

def check_even_or_odd(num):
    return num % 2 == 0

n = int(input("Quantos numeros voce vai digitar? "))

for i in range(1, n + 1):
    x = int(input("Digite um numero: "))

    if check_is_null(x):
        print("Nulo")
    else:
        if check_positive(x):
            print("Par positivo") if check_even_or_odd(x) else print("Impar positivo")
        else:
            print("Par negativo") if check_even_or_odd(x) else print("Impar negativo")
