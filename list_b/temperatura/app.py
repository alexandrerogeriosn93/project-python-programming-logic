def celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5.0 + 32.0

def fahrenheit_to_celsius(fahrenheit):
    return 5.0 / 9.0 * (fahrenheit - 32.0)

scale = str(input("Voce vai digitar a temperatura em qual escala (C/F)? ").upper())

match scale:
    case "F":
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"Temperatura equivalente em Celsius: {celsius:.2f}")
    case "C":
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"Temperatura equivalente em Fahrenheit: {fahrenheit:.2f}")
    case _:
        print("Escala inválida.")
