# Faça um programa que leia o comprimento do cateto oposto e do cateto adjascente
# de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

import math
cat_opost = float(input('Digite o valor do cateto oposto: '))
cat_adj = float(input('Digite o valor do cateto adjascente: '))

hypot = math.hypot(cat_opost, cat_adj)
print(f'O valor da hipotenusa é: {hypot}')
