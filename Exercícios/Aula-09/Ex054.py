# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
import datetime
maior = 0
menor = 0
for lista in range(0, 7):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite seu ano de nascimento: '))
    if (datetime.date.today().year - idade) > 18:
        maior += 1
    else:
        menor += 1

print(f'{maior} pessoas atingiram maioridade. {menor} pessoas ainda não atingiram maioridade.')
