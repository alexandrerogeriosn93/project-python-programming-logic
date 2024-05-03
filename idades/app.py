print("Dados da primeira pessoa", end="\n")
first_name = input("Nome: ")
first_age = int(input("Idade: "))

print("Dados da segunda pessoa", end="\n")
second_name = input("Nome: ")
second_age = int(input("Idade: "))

average = float((first_age + second_age)/2)

print(f"A idade média de {first_name} e {second_name} é de {average:.1f} anos")
