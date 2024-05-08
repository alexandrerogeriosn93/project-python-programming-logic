n = int(input("Quantos valores vai ter cada vetor? "))

vet_a = [0 for _ in range(n)]
vet_b = [0 for _ in range(n)]
vet_c = [0 for _ in range(n)]

print("Digite os valores do vetor A:")
for i in range(n):
    vet_a[i] = int(input())

print("Digite os valores do vetor B:")
for i in range(n):
    vet_b[i] = int(input())

for i in range(n):
    vet_c[i] = vet_a[i] + vet_b[i]

print("VETOR RESULTANTE:")
for i in range(n):
    print(f"{vet_c[i]}")
