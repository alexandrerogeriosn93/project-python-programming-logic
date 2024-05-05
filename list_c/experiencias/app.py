def calc_percent(animal, total):
    return (animal/total) * 100

def show_info(total, rabbit, mouse, frog, percent_rabbit, percent_mouse, percent_frog):
    text = f"""
Relatório final:

Total: {total} cobaias

Total de coelhos: {rabbit}
Total de ratos: {mouse}
Total de sapos: {frog}

Percentual de coelhos: {percent_rabbit:.2f}
Percentual de ratos: {percent_mouse:.2f}
Percentual de sapos: {percent_frog:.2f}"""

    return text

n = int(input("Quantos casos de teste serao digitados? "))

frog, mouse, rabbit = 0, 0, 0

for i in range(1, n + 1):
    quantity = int(input("Quantidade de cobaias: "))
    type_animal = tipo = str(input("Tipo de cobaia: ").upper())

    match type_animal:
        case "C":
            rabbit += quantity
        case "R":
            mouse += quantity
        case "S":
            frog += quantity

total = rabbit + mouse + frog

percent_rabbit = calc_percent(rabbit, total)
percent_mouse = calc_percent(mouse, total)
percent_frog = calc_percent(frog, total)

information = show_info(total, rabbit, mouse, frog, percent_rabbit, percent_mouse, percent_frog)

print(information)
