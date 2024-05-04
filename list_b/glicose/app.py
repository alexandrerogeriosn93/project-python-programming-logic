def glicose_classification(glicose):
    if(glicose <= 100):
        return "Normal"
    elif(glicose <= 140):
        return "Elevado"
    else:
        return "Diabetes"


glicose = float(input("Digite a medida da glicose: "))
classification = glicose_classification(glicose)

print(f"Classificação: {classification}")
