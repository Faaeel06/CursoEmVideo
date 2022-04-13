#  Faça um programa que leia um número qualquer e mostre o seu fatorial.

num = int(input('Digite o número: '))
termo = 1
fatorial = 1
while termo <= num:
    fatorial = fatorial * termo
    termo = termo + 1
print(f'O valor fatorial de {num} é: {fatorial}')
