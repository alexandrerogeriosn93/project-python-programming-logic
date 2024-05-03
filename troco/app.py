price = float(input("Preço unitário do produto: "))
quantity = int(input("Quantidade comprada: "))
money = float(input("Dinheiro recebido: "))

cashback = money - (price * quantity)

print(f"Troco = {cashback:.2f}")
