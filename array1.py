#construa usuário digitará o nome e o bairro 3 pessoas
#o nome e bairro das pessoas em ordem alfabética.
# #key=lambda função sem nome 

lista=[]

for i in range (0,3):
    nome = input("Digite seu nome: ")
    bairro = input("Digite seu bairro: ")
    lista.append([nome, bairro])

#ordem_alfa = []
lista.sort(key=lambda pessoa: pessoa[1])
print(f"{lista} essa é a ordem alfabetica")