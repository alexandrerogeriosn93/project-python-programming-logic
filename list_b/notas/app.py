first_grade = float(input("Digite a primeira nota: "))
second_grade = float(input("Digite a segunda nota: "))

final_grade = first_grade + second_grade

print(f"Nota final = {final_grade:.1f}")

if(final_grade < 60.0):
    print("Reprovado")
