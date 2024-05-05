num = int(input("Deseja a tabuada para qual valor? "))

multiplication_table = [print(f"{num} x {i} = {num * i}") for i in range(1, 11)]
