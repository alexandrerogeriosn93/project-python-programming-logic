from math import pow

n = int(input("Qual a ordem da matriz? "))
mat = [[0 for _ in range(n)] for _ in range(n)]
sum_positives = 0

for i in range(n):
    for j in range(n):
        mat[i][j] = float(input(f"Elemento [{i},{j}]: "))

for i in range(n):
    for j in range(n):
        if mat[i][j] > 0:
            sum_positives += mat[i][j]

print(f"\nSOMA DOS POSITIVOS: {sum_positives:.1f}\n")

line = int(input("Escolha uma linha: "))
print("LINHA ESCOLHIDA: ", end="")
for i in range(n):
    print(f"{mat[line][i]:.1f} ", end="")

column = int(input("\n\nEscolha uma coluna: "))
print("COLUNA ESCOLHIDA: ", end="")
for i in range(n):
    print(f"{mat[i][column]:.1f} ", end="")

print("\n\nDIAGONAL PRINCIPAL: ", end="")
for i in range(n):
    print(f"{mat[i][i]:.1f} ", end="")

print("\n\nMATRIZ ALTERADA:")
for i in range(n):
    for j in range(n):
        if mat[i][j] < 0:
            mat[i][j] = pow(mat[i][j], 2)
        print(F"{mat[i][j]:.1f} ", end="")
    print()
