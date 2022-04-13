# Programa que leia os dias alugados e os quilomêtros de um carro.
dia = int(input('O carro foi alugado por quantos dias? '))
km = float(input('Quantos quilômetros foram rodados? '))

print(f'O valor a ser pago pelo aluguel de {dia} dias e {km}Km rodados será:\nR$ {(dia*60)+(km*0.15):.2f}.')
