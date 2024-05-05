print("Digite dois numeros:")
x = int(input())
y = int(input())

if x > y:
    x, y = y, x

sum_odd = 0
for i in range(x+1, y):
    if i % 2 != 0 :
        sum_odd = sum_odd + i

print(f"SOMA DOS IMPARES = {sum_odd}")
