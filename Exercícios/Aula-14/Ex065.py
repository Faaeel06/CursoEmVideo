# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a media entre todos os
# valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao utilizador se ele quer ou não
# continuar a digitar valores.

perg = " "
soma = num = contador = 0
menor = 9999

while perg != "N":
    
    num = int(input("Digite um número: "))
    soma += num
    contador += 1
    
    if menor > num:
        menor = num
    perg = str(input("Deseja continuar: [Sim ou Não]: "))[0].upper()

print(f"Média: {soma/contador}", f"Menor: {menor}")
