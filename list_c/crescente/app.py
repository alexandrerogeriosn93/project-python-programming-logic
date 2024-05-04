x, y = [int(x) for x in input("Digite dois numeros: ").split(" ")]

res = f"Crescente" if x < y else f"Decrescente"

print(res)
