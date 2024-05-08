n = int(input("Serao digitados dados de quantos produtos? "))
names = [0 for _ in range(n)]
purchase_price = [0 for _ in range(n)]
sale_price = [0 for _ in range(n)]
percent_profit = [0 for _ in range(n)]
profit_below_ten_percent = 0
profit_between_ten_and_twenty_percent = 0
profit_above_twenty_percent = 0
vavlue_total_purchase = 0
value_total_sale = 0

for i in range(n):
	print(f"Produto {i + 1}:")
	names[i] = str(input("Nome: "))
	purchase_price[i] = float(input("Preco de compra: "))
	sale_price[i] = float(input("Preco de venda: "))

	percent_profit[i] = (sale_price[i] - purchase_price[i]) / purchase_price[i] * 100.0

	if percent_profit[i] < 10.0:
		profit_below_ten_percent += 1
	elif percent_profit[i] < 20.0:
		profit_between_ten_and_twenty_percent += 1
	else:
		profit_above_twenty_percent += 1

for i in range(n):
	vavlue_total_purchase += purchase_price[i]
	value_total_sale += sale_price[i]

total_profit = value_total_sale - vavlue_total_purchase

print("\nRELATORIO:")
print(f"Lucro abaixo de 10%: {profit_below_ten_percent}")
print(f"Lucro entre 10% e 20%: {profit_between_ten_and_twenty_percent}")
print(f"Lucro acima de 20%: {profit_above_twenty_percent}")
print(f"Valor total de compra: {vavlue_total_purchase:.2f}")
print(f"Valor total de venda: {value_total_sale:.2f}")
print(f"Lucro total: {total_profit:.2f}")
