n = int(input("Quantos elementos vai ter o vetor? "))
vet = [0 for _ in range(n)]
sum_numbers = 0

for i in range(n):
    vet[i] = float(input("Digite um numero: "))

for i in range(n):
    sum_numbers += vet[i]

average = sum_numbers/n

print(f"\nMEDIA DO VETOR = {average:.3f}")
print("ELEMENTOS ABAIXO DA MEDIA:")
for i in range(n):
    if vet[i] < average:
        print(f"{vet[i]}")
