# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
"""
1. Se o ano for uniformemente divisível por 4, vá para a etapa 2. Caso contrário, vá para a etapa 5.
2. Se o ano for uniformemente divisível por 100, vá para a etapa 3. Caso contrário, vá para a etapa 4.
3. Se o ano for uniformemente divisível por 400, vá para a etapa 4. Caso contrário, vá para a etapa 5.
4. O ano é bissexto (tem 366 dias).
5. O ano não é um ano bissexto (tem 365 dias)."""
import datetime

print('-=-' * 15)
print('=====Autenticador de Ano bissexto=====')
data = int(input('Digite o ano que deseja saber\n(Digite 0 para o ano atual): '))
if data == 0:
    data = datetime.date.today().year

if data % 4 == 0 and data % 100 != 0 or data % 400 == 0:
    print(f'O ano de {data} é um ano BISSEXTO.')
else:
    print(f'O ano de {data} NÃO é um ano BISSEXTO')
