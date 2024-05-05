alcool, gasolina, diesel = 0, 0, 0

while (code := int(input("Informe um codigo (1, 2, 3) ou 4 para parar: "))) != 4:
    match code:
        case 1:
            alcool += 1
        case 2:
            gasolina += 1
        case 3:
            diesel += 1

print(f"MUITO OBRIGADO\nAlcool: {alcool}\nGasolina: {gasolina}\nDiesel: {diesel}")
