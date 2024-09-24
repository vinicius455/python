peso = 105
altura = 1.85
imc = peso / altura **2
print("Seu IMC é de", round(imc,2))

if imc < 18.5:
    print("Baixo peso")
elif imc >= 18.5 and imc <= 24.9:
    print("Peso normal")
elif imc >= 25 and imc <= 29.9:
    print("Excesso de peso")
elif imc >= 30 and imc <= 34.9:
    print("Obesidade")
elif imc >= 35:
    print("Obesidade extrema")

