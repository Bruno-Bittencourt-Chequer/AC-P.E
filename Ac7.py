
 # EX01: AUMENTO DE SALÁRIO

a= float(input())
if (0<a<=400):
    reajuste=(((a*15)/100)+a)
    percentual= 15
    print("Novo salario: %.2f" %reajuste)
    print("Reajuste ganho: %.2f" %(reajuste-a))
    print("Em percentual: " + str(percentual) + " %")
elif(400<a<=800):
    reajuste=(((a*12)/100)+a)
    percentual= 12
    print("Novo salario: %.2f" %reajuste)
    print("Reajuste ganho: %.2f" %(reajuste-a))
    print("Em percentual: " + str(percentual) + " %")
elif(800<a<=1200):
    reajuste=(((a*10)/100)+a)
    percentual= 10
    print("Novo salario: %.2f" %reajuste)
    print("Reajuste ganho: %.2f" %(reajuste-a))
    print("Em percentual: " + str(percentual) + " %")
elif(1200<a<=2000):
    reajuste=(((a*7)/100)+a)
    percentual= 7
    print("Novo salario: %.2f" %reajuste)
    print("Reajuste ganho: %.2f" %(reajuste-a))
    print("Em percentual: " + str(percentual) + " %")
else:
    reajuste=(((a*4)/100)+a)
    percentual= 4
    print("Novo salario: %.2f" %reajuste)
    print("Reajuste ganho: %.2f" %(reajuste-a))
    print("Em percentual: " + str(percentual) + " %")


    #EX02: PARES ENTRE 5 NÚMEROS:

def valores_pares():
    numeros_pares = 0
    for i in range(5):
        valor = int(input("Digite o valor desejado: "))
        if valor % 2 == 0:
            numeros_pares += 1
    print(numeros_pares, "valores pares")

valores_pares()


#EX03: MÚLTIPLOS DE 13

soma=0
x=int(input())
y=int(input())
if (y>x):
    for n in range(x,(y+1)):
        if (n%13!=0):
            soma+=n
if (x>y):
    for n in range(y,(x+1)):
        if (n%13!=0):
            soma+=n
print(soma)

#EX04: PREENCHIMENTO DE VETOR I

V = int(input())
N = [0]*10
N[0] = V

for i in range(1, 10):
    N[i] = N[i-1]*2

for i in range(10):
    print(f"N[{i}] = {N[i]}")


#EX05: MENOR E POSIÇÃO:

n = int(input())  
x = []

for _ in range(n):
    x.append(int(input()))
menor_valor = x[0]
posicao = 0
for i in range(1, n):
    if x[i] < menor_valor:
        menor_valor = x[i]
        posicao = i

print("Menor valor:", menor_valor)
print("Posicao:", posicao)



#EX06: COLUNA NA MATRIZ:


coluna = int(input())
operacao = input()

matriz = []
for _ in range(12):
    linha = []
    for _ in range(12):
        linha.append(float(input()))

    matriz.append(linha)
coluna_selecionada = []
for i in range(12):
    coluna_selecionada.append(matriz[i][coluna])

resultado = 0
if operacao == 'S':
    resultado = sum(coluna_selecionada)
elif operacao == 'M':
    resultado = sum(coluna_selecionada) / len(coluna_selecionada)

print(round(resultado, 1))


#EX07: ORDENAÇÃO POR TAMANHO:

def ordenar_strings(strings):
    return sorted(strings, key=lambda x: (len(x), strings.index(x)))

def main():
    casos_teste = int(input())
    for _ in range(casos_teste):
        conjunto_strings = input().split()
        conjunto_strings_ordem = ordenar_strings(conjunto_strings)
        print(' '.join(conjunto_strings_ordem))

if __name__ == "__main__":
    main()
