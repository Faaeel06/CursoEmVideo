# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e
# R$0,45 para viagens mais longas.

print('-=-' * 15)
print('====CALCULADORA DE PASSAGEM====')
distancia = float(input('Digite a distância percorrida: '))
if distancia <= 200:
    valor_passagem = distancia * 0.50
    print(f'O percurso foi de {distancia}Km.\n'
          f'O valor a ser pago na passagem é: R${valor_passagem:.2f}')
else:
    valor_passagem = distancia * 0.45
    print(f'O percurso foi de {distancia}KM.\n'
          f'O valor a ser pago na passagem é: R${valor_passagem:.2f}')

print('-=-' * 15)
