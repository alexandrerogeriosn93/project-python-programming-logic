n = int(input("Quanto numeros voce vai digitar? "))
vet = [0 for x in range(n)]

for i in range(n):
    vet[i] = float(input("Digite um numero: "))

max_value = max(vet)
position = vet.index(max_value)

print(f"\nMAIOR VALOR = {max_value:.1f}")
print(f"POSICAO DO MAIOR VALOR = {position}")
