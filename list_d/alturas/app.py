n = int(input("Quantas pessoas serao digitadas? "))

names = [0 for _ in range(n)]
ages = [0 for _ in range(n)]
heights = [0 for _ in range(n)]
under_sixteen = 0
total_height = 0

for i in range(n):
	print(f"Dados da {i+1}ª pessoa:")
	names[i] = input("Nome: ")
	ages[i] = int(input("Idade: "))
	heights[i] = float(input("Altura: "))

for i in range(n):
	if ages[i] < 16:
		under_sixteen += 1
		total_height += heights[i]

average_height = total_height / under_sixteen
percent_under_sixteen = (float(under_sixteen) / n) * 100.0

print(f"\nAltura media = {average_height:.2f}")
print(f"Pessoas com menos de 16 anos: {percent_under_sixteen:.1f}%")

for i in range(n):
	if ages[i] < 16:
		print(names[i])
