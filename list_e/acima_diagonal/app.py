n = int(input("Qual a ordem da matriz? "))
mat = [[0 for _ in range(n)] for _ in  range(n)]
sum_above_diagonal = 0

for i in range(n):
    for j in range(n):
        mat[i][j] = int(input(f"Elemento [{i},{j}]: "))

for i in range(n):
    for j in range(n):
        if j > i:
            sum_above_diagonal += mat[i][j]

print(f"SOMA DOS ELEMENTOS ACIMA DA DIAGONAL PRINCIPAL = {sum_above_diagonal}")
