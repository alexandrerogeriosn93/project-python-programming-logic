m = int(input("Qual a quantidade de linhas da matriz? "))
n = int(input("Qual a quantidade de colunas da matriz? "))
mat = [[0 for _ in range(n)] for _ in range(m)]
vet = [0 for _ in range(m)]

for i in range(m):
    print(f"\nDigite os elementos da {i + 1}ª linha:")
    for j in range(n):
        mat[i][j] = float(input())

for i in range(m):
    sum_line = 0
    for j in range(n):
        sum_line += mat[i][j]
    vet[i] = sum_line

print("\nVETOR GERADO:")
for i in range(m):
    print(f"{vet[i]:.1f}")
