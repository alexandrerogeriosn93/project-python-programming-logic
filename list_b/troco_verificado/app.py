def calc_cashback(money, value):
    if(money < value):
        return f"Dinheiro insuficiente. Faltam {(value - money):.2f} reais"
    
    return f"Troco = {(money - value):.2f} reais"

price = float(input("Preço unitário do produto: "))
quantity = int(input("Quantidade comprada: "))
money = float(input("Dinheiro recebido: "))

value = price * quantity

cashback = calc_cashback(money, value)

print(cashback)
