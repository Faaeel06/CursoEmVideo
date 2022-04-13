# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
peso_max = 0
peso_min = 0
for analise in range(1, 6):
    peso = float(input(f'Digite o peso da {analise}° pessoa: '))
    if analise == 1:
        peso_max = peso
        peso_min = peso
    else:
        if peso > peso_max:
            peso_max = peso
        if peso < peso_min:
            peso_min = peso


print(f'O maior peso foi {peso_max}Kg e o menor peso foi {peso_min}Kg.')
