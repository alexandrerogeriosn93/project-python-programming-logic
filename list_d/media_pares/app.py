n = int(input("Quantos elementos vai ter o vetor? "))
vet = [0 for x in range(n)]
sum_even, quantity_even = 0, 0

for i in range(n):
    vet[i] = int(input("Digite um numero: "))

    if vet[i] % 2 == 0:
        sum_even += vet[i]
        quantity_even += 1

try:
    average_even = sum_even/quantity_even
    print(f"MEDIA DOS PARES = {average_even:.1f}")
except ZeroDivisionError:
    print("NENHUM NUMERO PAR")
