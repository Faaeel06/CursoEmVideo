# Crie um programa que leia dois valores e mostre um menu na tela:
# 1 - somar
# 2 - multiplicar
# 3 - maior
# 4 - novos números
# 5 - sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep
print('Vamos começar? ')
sleep(0.5)
print('''
      MENU
      1 - SOMAR
      2 - MULTIPLICAR
      3 - MAIOR
      4 - NOVOS NÚMEROS
      5 - SAIR DO PROGRAMA
      ''')
sleep(0.5)
num_1 = int(input('Digite o primeiro termo: '))
num_2 = int(input('Digite o segundo termo: '))

while True:
    menu = int(input('Digite a opção do menu que deseja execultar: '))
    result = ''
    if menu == 1:
        result = num_1 + num_2
    elif menu == 2:
        result = num_1 * num_2
    elif menu == 3:
        if num_1 > num_2:
            result = num_1
        else:
            result = num_2
    elif menu == 4:
        num_1 = int(input('Digite o primeiro termo: '))
        num_2 = int(input('Digite o segundo termo: '))
    elif menu == 5:
        break
    print(result)
