""""
Faça um programa que receba três notas, calcule sua média aritmética simples e apresente na tela uma das seguintes informações:

A mensagem “Aprovado”, se a média alcançada for maior ou igual a sete;
A mensagem “Reprovado”, se a média for menor do que sete;
A mensagem “Aprovado com Distinção”, se a média for igual a dez;
A mensagem “Nota inválida!” toda vez que for inserido um valor inválido.
"""

def nota_e_valida(nota):
        return 0<= nota <=10
def aprovacao(n1,n2,n3):
    M=(n1+n2+n3)/3
    if nota_e_valida(n1) and nota_e_valida(n2) and nota_e_valida(n3):
        if 7 <= M <10 :
            print("Aprovado")
    elif 0 < M < 10 :
        print("Reprovado")
    elif M==10: 
        print(" Aprovado com Distinção")
    else:
        print("Nota Inválida")

aprovacao(8,9,7)

