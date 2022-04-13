# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, consseno e tangente desse ângulo
import math

valor = float(input('Digite o ângulo: '))
angulo = math.radians(valor)
seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)

print(f'Para o ângulo: {valor}°\n'
      f'Seno vale: {seno:.2f}...;\n'
      f'Cosseno vale: {cosseno:.2f}...; e\n'
      f'Tangente vale: {tangente:.2f}... .')
