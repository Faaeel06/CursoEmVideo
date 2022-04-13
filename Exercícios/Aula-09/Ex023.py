#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
"""
numero = input('Digite um número: ').strip()
print(f'O número: {numero};\n'
      f'Na cada dos milhares: {numero[0]};\n'
      f'Na casa das centenas:{numero[1]};\n'
      f'Na casa das dezenas: {numero[2]};\n'
      f'Na casa das unidades: {numero[3]}.')
"""
num = int(input('informe um número: '))
unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10

print(f'O número: {numero};\n'
      f'Na cada dos milhares: {milhar};\n'
      f'Na casa das centenas:{centena};\n'
      f'Na casa das dezenas: {dezena};\n'
      f'Na casa das unidades: {unidade}.')
