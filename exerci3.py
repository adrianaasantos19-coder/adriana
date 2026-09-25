#usuário digitará cinco números 
#deverá colocar esses números dentro do vetor em ordem crescente.

lista = []
for i in range (0,5):
    numero = float(input("digite um número: "))
    lista.append(numero)
list.sort()
print(f"{lista} estão em ordem")