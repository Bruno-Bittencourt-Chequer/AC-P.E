#EXERCÍCIO 01- FÓRMULA DE BHÁSKARA

import math

a = float(input("Digite o primeiro parâmetro: "))
b = float(input("Digite o segundo parâmetro: "))
c = float(input("Digite o terceiro parâmetro: "))

#Cálculo do delta
D = b**2 - 4*a*c

if D < 0:
    print("Não é possível continuar a equação")
elif D == 0:
    x = -b / (2*a)
    print("Duas raízes idênticas no valor de:", x)
else:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)

    print("Resultado: x1 é igual a:", x1, "e x2 é igual a:", x2)

   
   
    #EXERCÍCIO 02-ANO BISSEXTO

ano=int(input("Escreva o ano que deseja: "))
bissexto= (ano % 4== 0 and ano % 100==0) or (ano % 400 !=0)
print(" O ano", ano, "é bissexto?", bissexto)

