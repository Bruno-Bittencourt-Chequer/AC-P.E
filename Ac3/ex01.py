#EX01: IDENTIFICAÇÃO DE TRIÂNGULOS

def determina_tipo_triangulo():
    l1=float(input("Digite o primeiro lado:"))
    l2=float(input("Digite o segundo lado:"))
    l3=float(input("Digite o terceiro lado:"))
    if l1==l2==l3:
            print("O Triângulo é Equilátero")
    elif l1!=l2!=l3!=l1:
            print("O Triângulo é  Escaleno")
    elif l1==l2 and l2!=l3:
            print(("O Triângulo é Isósceles"))
    else:
            print("Não é um Triângulo")

determina_tipo_triangulo()