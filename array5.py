# Construa usuário digitará o nome e a idade de dez
# pessoas e o programa escreverá o nome do usuário mais novo.
#key=lambda função sem nome 

lista=[]

for i in range (4):
    nome = input("Digite seu nome: ")
    idade = int(input("Digite seu idade: "))
    lista.append([nome, idade])

mais_novo= min(lista, key=lambda pessoa: pessoa [1])
print(f"O usuario mais novo é:{mais_novo[0]}")







# for i in range(1,len(lista)):
    # if lista[i][1] <lista[mais_novo][1]:
#         mais_novo = i
# print(f" O usuário mais novo é: {lista[mais_novo][0]}")

