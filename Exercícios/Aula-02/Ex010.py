# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar
#Considere: US$1,00 = R$ 5,25

aporte = float(input('Digite quanto você tem na carteira: R$ '))

print(f'Com o valor R${aporte:.2f}. Você conseguirá comprar US${(aporte/5.25):.2f}.')
