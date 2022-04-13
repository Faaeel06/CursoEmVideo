# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# - O primero valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais
print(f'{"=" * 20:>}', 'COMPARADOR NÚMERICO', f'{"=" * 20:>}')

NUM_1 = float(input('Digite o primeiro valor: '))
NUM_2 = float(input('Digite o segundo valor: '))

if NUM_1 > NUM_2:
    print('O primeiro valor é maior.')
elif NUM_1 < NUM_2:
    print('O segundo valor é maior.')
else:
    print('Não existe valor maior, ambos são iguais.')
