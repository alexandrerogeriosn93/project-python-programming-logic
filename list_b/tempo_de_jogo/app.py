initial_hour = int(input("Hora inicial: "))
final_hour = int(input("Hora final: "))
duration = final_hour - initial_hour if final_hour > initial_hour else 24 - (initial_hour - final_hour)

print(f"O jogo durou {duration} hora(s)")
