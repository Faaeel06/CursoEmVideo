# Faça um algoritmo que leia o preço de um produto e mostre seu nobo preço, com 5% de desconto

preco = float(input('digite o valor do produto: R$ '))
print(f'O produto tinha o valor R${preco}.'
      f'O seu novo preço com 5% de desconto será R${(preco-(preco*0.05)):.2f}!')
