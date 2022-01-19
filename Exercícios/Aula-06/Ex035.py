# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
# se elas podem ou não formar um triângulo.

lado1 = float(input('Digite o valor do primeiro lado: '))
lado2 = float(input('Digite o valor do segundo lado: '))
lado3 = float(input('Digite o valor do terceiro lado: '))

if (lado1 - lado2) < lado3 and (lado3 - lado1) < lado2 and (lado3 - lado2) < lado1:
    print('Pode formar um triângulo.')
else:
    print('Não pode formar um trângulo.')
