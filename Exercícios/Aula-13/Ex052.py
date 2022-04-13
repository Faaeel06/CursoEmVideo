# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
validacao = ''
conferir = 0
numero = int(input('Digite um número: '))
for validador in range(1, numero + 1):
    if numero % validador == 0:
        conferir += 1
        if conferir == 2:
            validacao = 'é PRIMO'
        else:
            validacao = 'não é PRIMO'

print(f'O número {numero} é divisível {conferir} vezes e por isso ele {validacao}.')