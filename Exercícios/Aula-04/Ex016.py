# Crie um programa que leia um número Real qualquer r mostre na tela a sua porção inteira
# Ex: Digite um número: 6.127
# O número 6.127 tem a parte inteira 6.

import math

num = float(input('Digite um número real qualquer: '))
print(f'A porção inteira do número {num} é igual à: {math.trunc(num)}')
