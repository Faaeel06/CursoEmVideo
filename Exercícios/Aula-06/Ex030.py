# Crie um programa que leia um número inteiro qualquer e mostre na tela se ele é par ou ímpar.

print('-=-' * 15)
print('=====PAR ou ÍMPAR=====')
numero = int(input('Digite o número: '))

if numero % 2 == 0:
    print('O número digitado é PAR.')
else:
    print('O número digitado é ÍMPAR.')

print('-=-' * 15)
