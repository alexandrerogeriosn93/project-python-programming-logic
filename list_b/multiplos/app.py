x, y = [int(x) for x in input("Digite dois numeros inteiros: ").split(" ")]

try:
    if(x % y == 0 or y % x == 0):
        print("Sao multiplos")
    else:
        print("Nao sao multiplos")
except ZeroDivisionError:
    print("Impossível dividir por zero")
