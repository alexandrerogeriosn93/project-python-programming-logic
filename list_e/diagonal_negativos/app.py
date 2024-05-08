n = int(input("Qual a ordem da matriz? "))
mat = [[0 for _ in range(n)] for _ in range(n)]
negatives = 0

for i in range(0, n):
    for j in range(0, n):
        mat[i][j] = int(input(f"Elemento [{i},{j}]: "))
        
        if mat[i][j] < 0:
            negatives += 1

print("\nDIAGONAL PRINCIPAL:")
for i in range(0, n):
    print(f"{mat[i][i]} ", end="")

print(f"\nQUANTIDADE DE NEGATIVOS = {negatives}")
