m = int(input("Qual a quantidade de linhas da matriz? "))
n = int(input("Qual a quantidade de colunas da matriz? "))
mat = [[0 for _ in range(n)] for _ in range(m)]

for i in range(m):
    for j in range(n):
        mat[i][j] = int(input(f"Elemento [{i},{j}]: "))

print("\nVALORES NEGATIVOS:")
for i in range(m):
    for j in range(n):
        if mat[i][j] < 0:
            print(f"{mat[i][j]}")
