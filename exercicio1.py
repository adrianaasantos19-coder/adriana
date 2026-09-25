#usuário para digitar quatro num
#programa deve pedir um num adicional e ver se está na lista
#informe em qual posição da primeira vez
#index prucura o num na lista

lista=[]
for i in range (0,4):
    n=int(input("Digite um número: "))
    lista.append(n)

n1=int(input("Digite um número: "))

if n1 in lista:
    posicao = lista.index(n1)
    print(f"Esse número já apareceu na posição {posicao +1}")
