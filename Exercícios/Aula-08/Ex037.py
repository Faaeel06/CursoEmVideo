# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a ase de conversão:
# 1 para binario
# 2 para octal
# 3 para hexadecimal

print(f'{"=" * 20:>}', 'CONVERSOR DE BASE NÚMERICA', f'{"=" * 20:>}')

num_convert = int(input('Digite o valor que quer converter[Em decimal]: '))
lista = ["1 - para converter para binário", "2 - para converter para octal", "3 - para converter para hexacdecimal"]
print(lista[0])
print(lista[1])
print(lista[2])
opcao = int(input('Digite a opção: '))

if opcao == 1:
    converter = bin(num_convert)
    print(f'O número {num_convert} convertido em binário é: {converter[2:]}')
elif opcao == 2:
    converter = oct(num_convert)
    print(f'O número {num_convert} convertido em octal é: {converter[2:]}')
elif opcao == 3:
    converter = hex(num_convert)
    print(f'O número {num_convert} convertido em hexadecimal é: {converter[2:]}')
else:
    print('Opção inválida.')
