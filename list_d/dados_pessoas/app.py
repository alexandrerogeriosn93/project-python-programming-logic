n = int(input("Quantas pessoas serao digitadas? "))
heights = [0 for _ in range(n)]
genres = [0 for _ in range(n)]
men, women, women_height = 0, 0, 0

for i in range(n):
    heights[i] = float(input(f"Altura da {i + 1}ª pessoa: "))
    genres[i] = str(input(f"Genero da {i + 1}ª pessoa: ").upper())

    match genres[i]:
        case "F":
            women_height += heights[i]
            women += 1
        case "M":
            men += 1

max_height = max(heights)
min_heigth = min(heights)
average_women_height = women_height/women

print(f"Menor altura = {min_heigth:.2f}")
print(f"Maior altura = {max_height:.2f}")
print(f"Media das alturas das mulheres = {average_women_height:.2f}")
print(f"Numero de homens = {men}")
