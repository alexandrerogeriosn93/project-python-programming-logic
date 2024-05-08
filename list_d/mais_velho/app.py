n = int(input("Quantas pessoas voce vai digitar? "))
names = [0 for x in range(n)]
ages = [0 for x in range(n)]

for i in range(n):
    print(f"Dados da {i + 1}a pessoa:")
    names[i] = str(input("Nome: "))
    ages[i] = int(input("Idade: "))

max_age = ages.index(max(ages))

print(f"PESSOA MAIS VELHA: {names[max_age]}")
