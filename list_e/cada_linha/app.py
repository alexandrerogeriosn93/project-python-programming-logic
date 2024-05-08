n = int(input("Qual a ordem da matriz? "))
mat = [[0 for _ in range(n)] for _ in range(n)]
vet = [0 for _ in range(n)]

for i in range(n):
    for j in range(n):
        mat[i][j] = int(input(f"Elemento [{i},{j}]: "))

for i in range(n):
    highest_value = mat[i][0]
    for j in range(n):
        if mat[i][j] > highest_value:
            highest_value = mat[i][j]
    vet[i] = highest_value

print("MAIOR ELEMENTO DE CADA LINHA:")
for i in range(n):
    print(f"{vet[i]}")
