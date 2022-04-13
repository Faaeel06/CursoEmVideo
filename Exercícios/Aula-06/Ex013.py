# Faça um algoritmo que leia o sálario de um funcionário e mostre seu novo salário, com 15% de aumento

salario = float(input('Digite o sálario atual: R$ '))
print(f'O sálario sofreu reajuste. Antes era R${salario}.'
      f'Agora com aumento de 15% será R${(salario+(salario*0.15)):.2f}.')
