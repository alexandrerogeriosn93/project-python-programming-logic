from statistics import mean

ages = []

print("Digite as idades:", end="\n")
age = int(input())

while age >= 0:
    ages.append(age)
    age = int(input())

print("Impossível calcular") if len(ages) == 0 else print(f"Media = {mean(ages):.2f}")
