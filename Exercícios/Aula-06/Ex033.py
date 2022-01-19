# Faça um programa que leia três números e mostre qual é o maior e qual o menor.

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))
maior = num1
menor = num1
if num1 != num2 != num3:
    if num3 < num2 > num1:
        maior = num2
    elif num2 < num3 > num1:
        maior = num3
    print(f'O maior número é: {maior}')
    if num3 > num2 < num1:
        menor = num2
    elif num2 > num3 < num1:
        menor = num3
    print(f'O menor número é: {menor}')

elif num1 == num2 == num3:
    maior = menor
    print('Todos nos números são iguais.')
