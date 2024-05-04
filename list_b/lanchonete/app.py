def check_code(code):
    return code >= 1 and code <= 5

def calc_total(code, quantity):
    if check_code(not code):
        return "Opção inválida"
    
    value = ""

    match code:
        case 1:
            value = 5.00
        case 2:
            value = 3.50
        case 3:
            value = 4.80
        case 4:
            value = 8.90
        case 5:
            value = 7.32

    return quantity * value

code, quantity = [int(x) for x in input("Digite o código do produto e a quantidade: ").split(" ")]

total = calc_total(code, quantity)

if total == "Opção inválida":
    print(f"{total}")
else:
    print(f"Total a pagar: R$ {total:.2f}")
