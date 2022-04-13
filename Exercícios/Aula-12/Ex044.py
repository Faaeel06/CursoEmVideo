# Elabore um programa que calcule o valor a ser pago por um produto. considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista cartão: 5% de desconto
# - Em até 2x no cartão: Preço normal
# - 3X ou mais no cartão: 20% de juros

print(f'{"=" * 20:>}', 'CAIXA FINANCEIRO', f'{"=" * 20:>}')
pagamento = ['1 - Dinheiro', '2 - Débito', '3 - Cheque', '4 - Cartão (À vista)', '5 - Cartão (Em até 2x)', '6 - Cartão (3x ou acima)']
print(f'{pagamento[0]}\n{pagamento[1]}\n{pagamento[2]}\n{pagamento[3]}\n{pagamento[4]}\n{pagamento[5]}\n')

print(f'{"=" * 20:>}', 'PAGAMENTO', f'{"=" * 20:>}')
valor = float(input('Digite o valor a ser pago: R$ '))
forma_pagamento = int(input('Digite a forma de pagamento[Entre 1 e 6]:  '))
preco = ''
juros = ' '
parcelamento = ''
dividido = ''
condicao = ''
if forma_pagamento == 1:
   preco = valor - (valor * 0.10)
   juros = ['Desconto', '10%']
elif forma_pagamento == 2:
       preco = valor - (valor * 0.10)
       juros = ['Desconto', '10%']
elif forma_pagamento == 3:
   preco = valor - (valor * 0.10)
   juros = ['Desconto', '10%']
elif forma_pagamento == 4:
    preco = valor-(valor * 0.05)
    juros = ['Desconto', '5%']
elif forma_pagamento == 5:
    preco = valor
    parcelamento = 2
    dividido = preco / parcelamento
    juros = ['Sem Desconto', ' ']
    condicao = f'Sua compra foi parcelada em {parcelamento}x e o valor da parcela será: R${dividido:.2f}'
elif forma_pagamento == 6:
    preco = valor + (valor * 0.20)
    parcelamento = int(input('Em quantas parcelas deseja dividir? '))
    dividido = preco / parcelamento
    juros = ['Acréscimo', '20%']
    condicao = f'Sua compra foi parcelada em {parcelamento}x e o valor da parcela será: R${dividido:.2f}'
else:
    print('Forma de pagamento inválida.')


print(f'{"=" * 20:>}', 'INFORME DE PAGAMENTO', f'{"=" * 20:>}')

print(f'Valor do produto: R$ {valor:.2f}\n'
      f'Forma de pagamemento: {pagamento[forma_pagamento - 1]}\n'
      f'Valor final: R${preco:.2f}\n'
      f'{juros[0]}: {juros[1]}\n'
      f'{condicao}')

