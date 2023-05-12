#funcao calcula_inss(salario, aliquota)
def calcula_inss(salario, aliquota):
    return salario * aliquota/100
#programa principal
print("inicio do programa ")
salariobase = float(input("digite qual valor do seu salario:"))
inss = 0
#processamento - calculo do inss
if salariobase <= 1320:
    inss = calcula_inss(salariobase, 7.5)
elif salariobase > 1320.01 and salariobase <=2571.49:
    inss = calcula_inss(salariobase,9)
elif salariobase >= 2571.30 and salariobase <=3856.9:
    inss = calcula_inss(salariobase, 12)
elif salariobase >= 3856.95 and salariobase <= 7507.49:
    inss = calcula_inss(salariobase,14)
else:
    inss = 876.95
salario = salariobase - inss
#saida de dados
print("salario base:" , salariobase)
print("inss", inss)
print("salario - inss: ", salario)
print("fim do programa ")