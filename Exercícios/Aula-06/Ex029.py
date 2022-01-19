# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.
import time
print('-=-' * 15)
print('====Radar Digital====')
time.sleep(0.5)
velocidade = float(input('QUal a velocidade do carro? '))

if velocidade > 80:
    multa = velocidade - 80
    valor_multa = multa * 7.00
    print(f'Você ultrapassou a velocidade permitida.\n'
          f'A velocidade acima da média foi {multa}km/h.\n'
          f'O valor a ser pago na multa é : R${valor_multa:.2f}.')
else:
    print('Você está dentro da velocidade permitida.\n'
          'Tenha uma ótima viagem!')
print('-=-' * 15)
