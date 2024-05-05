n = int(input("Quantos casos voce vai digitar? "))

for i in range(1, n + 1):
    numerator = int(input("Entre com o numerador: "))
    denominator = int(input("Entre com o denominador: "))

    try:
        division = numerator/denominator
        print(f"Divisão = {division:.2f}")
    except ZeroDivisionError:
        print("Divisão impossível")
