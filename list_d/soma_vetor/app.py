n = int(input("Quantos numeros voce vai digitar? "))
vet = [0 for x in range(n)]
sum_vet = 0

for i in range (0, n):
    vet[i] = float(input("Digite um numero: "))

print("\nVALORES = ", end="")

for i in range(0, n):
    print(f"{vet[i]:.1f} ", end="")

for i in range(0, n):
    sum_vet = sum_vet + vet[i]

media = sum_vet/n

print(f"\nSOMA = {sum_vet:.2f}\nMEDIA = {media:.2f}")
