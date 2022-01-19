# Escreva um programa que para aprovar o empréstimo bancário para compra de uma casa.
# O programa vai perguntar o valor da casa, o sálario do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do sálario ou então o empréstimo será negado.
print(f'{"=" * 20:>} CENTRAL DE EMPRÉSTIMOS {"=" * 20:>}')
nome = str(input('Digite seu nome completo: '))

print(f'{"=" * 20:>} CALCULADORA DE EMPRÉSTIMOS {"=" * 20:>}')

valor_casa = float(input('Digite o valor da casa: R$ '))
valor_salario = float(input('Digite o seu o valor bruto do sálario: R$ '))
periodo_pagamento = int(input('Deseja pagar em quantos anos: '))

prestacao = valor_casa / (periodo_pagamento * 12)

if prestacao <= valor_salario * 0.3:
    print(f'Sr.(a), {nome}\n'
          f'Seu empréstimo foi aprovado.\n'
          f'O valor da prestação é: R${prestacao:.2f}')
else:
    print(f'Sr.(a), {nome}\n'
          f'Seu empréstimo foi negado.\n'
          f'O valor da prestação é: R${prestacao:.2f}\n'
          f'O equivalente a 30% do seu sálario é: R${(valor_salario *0.3):.2f}. e está abaixo do valor da prestação.')
