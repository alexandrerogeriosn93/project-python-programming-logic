n = int(input("Quantos alunos serao digitados? "))
names = [0 for _ in range(n)]
vet_first_grade = [0 for _ in range(n)]
vet_second_grade = [0 for _ in range(n)]
vet_average = [0 for _ in range(n)]

for i in range(n):
    print(f"Digite nome, primeira e segunda nota do {i + 1}o aluno:")
    names[i] = str(input())
    vet_first_grade[i] = float(input())
    vet_second_grade[i] = float(input())
    vet_average[i] = (vet_first_grade[i] + vet_second_grade[i])/2

print("Alunos aprovados:")
for i in range(n):
    if vet_average[i] >= 6:
        print(f"{names[i]:.1f}")
