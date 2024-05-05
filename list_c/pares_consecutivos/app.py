while (x := int(input("Digite um numero inteiro: "))) != 0:
    soma = 0
    if x % 2 != 0:
        x = x + 1
    soma = 5 * x + 20
    print(f"SOMA = {soma}")
