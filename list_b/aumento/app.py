def calc_increase_salary(salary, percent):
    return (salary * percent) / 100

salary = float(input("Digite o salario da pessoa: "))

if salary <= 1000:
    percent = 20
elif salary <= 3000:
    percent = 15
elif salary <= 8000:
    percent = 10
else:
    percent = 5

adjust_salary = calc_increase_salary(salary, percent)
new_salary = salary + adjust_salary

print(f"Novo salário = R$ {new_salary:.2f}\nAumento = R$ {adjust_salary:.2f}\nPorcentagem = {percent} %")
