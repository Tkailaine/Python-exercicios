#Escreva uma expressão para determinar se uma pessoa deve ou não pagar imposto.
#Considere que pagam imposto pessoas cujo salário é maior queR$ 1.200,00.

salario = float(input("Digite seu salário: "))
if salario > 1200:
    print("Você deve pagar imposto de renda.")
else:
    print("Você não deve pagar imposto de renda.")