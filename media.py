#usuário para digitar quatro num
#calcular a media
#quantas e quais notas ficaram acima da média calculada.

lista = []

for _ in range(0,4):
    nota = float(input("digite um nota: "))
    lista.append(nota)

media = sum(lista)/len(lista)
acima_media =[]
for nota in lista:
    if nota < media:
        acima_media.append(nota)
        print(f"qtd notas acima média:{len(acima)}")