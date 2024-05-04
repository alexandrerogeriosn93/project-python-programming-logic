x = float(input("Valor de X: "))
y = float(input("Valor de Y: "))
coordinate = ""

if x == 0 and y == 0:
    coordinate = "Origem"
elif x == 0:
    coordinate = "Eixo Y"
elif y == 0:
    coordinate = "Eixo X"
elif x > 0 and y > 0:
    coordinate = "Q1"
elif x < 0 and y > 0:
    coordinate = "Q2"
elif x < 0 and y < 0:
    coordinate = "Q3"
else:
    coordinate = "Q4"

print(f"{coordinate}")
