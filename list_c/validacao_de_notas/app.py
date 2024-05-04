def validate_grade(grade):
    return grade < 0 or grade > 10

first_grade = float(input("Digite a primeira nota: "))

while validate_grade(first_grade):
    first_grade = float(input("Valor invalido! Tente novamente: "))

second_grade = float(input("Digite a segunda nota: "))

while validate_grade(second_grade):
    second_grade = float(input("Valor invalido! Tente novamente: "))

average = (first_grade + second_grade)/ 2

print(f"MEDIA = {average:.2f}")
