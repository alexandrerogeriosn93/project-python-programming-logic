n = int(input("Quantos numeros voce vai digitar? "))
vet = [0 for x in range(n)]
quantity_even = 0

for i in range(n):
    vet[i] = int(input("Digite um numero: "))

print("\nNUMEROS PARES:")
for i in range(n):
    if vet[i] % 2 == 0:
        print(f"{vet[i]} ", end="")
        quantity_even += 1

print(f"\n\nQUANTIDADE DE PARES = {quantity_even}")
