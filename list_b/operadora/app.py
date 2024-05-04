minutes = int(input("Digite a quantidade de minutos: "))

base_value = 50.0
value = base_value if minutes < 100 else base_value + ((minutes - 100) * 2)

print(f"Valor a pagar: R$ {value:.2f}")
