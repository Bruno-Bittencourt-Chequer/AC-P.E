def soma(a,b):
    return a+b

def subtracao(a,b):
    return a-b

def mult(a,b):
    return a*b

def divisao(a,b):
    return a/b


def calculo():
    n1=float(input("Informe o primeiro número: "))
    n2=float(input("Informe o segundo número:  "))
    op=str(input("Informe a operação:soma,subtracao,multi,divisao:  "))

    if op=="soma":
        resultado= soma(n1,n2)
    elif op=="subtraçao":
        resultado=subtracao(n1,n2)
    elif op=="mult":
        resultado=mult(n1,n2)
    elif op=="divisao":
        resultado=divisao(n1,n2)
    else:
        print("Operação Inválida")
        return
    return f"Resultado:{resultado}"
    
    
    
print(calculo())


