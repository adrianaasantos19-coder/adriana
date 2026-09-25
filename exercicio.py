#usuário digitará sete números 
# na tela exibi quantos deles são pares e quantos são ímpares.


lista = []
for i in range (0,7):
    numero = float(input("Digite um número: "))
    lista.append(numero)

par = 0 
impar = 0
for numero in lista:
    if numero % 2 == 0:
        par +=1
    else:
        impar +=1 

print(f"{par} são pares, {impar} são impares")