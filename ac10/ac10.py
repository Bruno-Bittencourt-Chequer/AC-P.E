

#CAMISETAS:

def main():
    while True:
        N = int(input())
        if N == 0:
            break

        camisetas = []
        for _ in range(N):
            nome = input()
            cor, tamanho = input().split()
            camisetas.append((cor, tamanho, nome))

        camisetas.sort(key=lambda x: (x[0], -ord(x[1]), x[2]))

        for camiseta in camisetas:
            print(f'{camiseta[0]} {camiseta[1]} {camiseta[2]}')  
        print()  

if __name__ == "__main__":
    main()


#ESCADA DO DINF:


import math

def main():
    while True:
        try:
            N = int(input())
            H, C, L = map(int, input().split())
        except EOFError:
            return

        hipotenusa = math.sqrt(H**2 + C**2) * N / 100  # converte para metros
        largura = L / 100  # converte para metros

        area = hipotenusa * largura

        print(f'{area:.4f}')

if __name__ == "__main__":
    main()
