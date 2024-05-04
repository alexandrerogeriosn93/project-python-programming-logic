name = input("Nome: ")
value = float(input("Valor por hora: "))
hours = int(input("Horas trabalhadas: "))

payment = value * hours

print(f"O pagamento para {name} deve ser {payment:.2f}")
