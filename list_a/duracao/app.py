duration = int(input("Digite a duração em segundos: "))

hours = duration//3600
rest = duration%3600
minutes = rest//60
seconds = rest%60

print(f"{hours}:{minutes}:{seconds}")
