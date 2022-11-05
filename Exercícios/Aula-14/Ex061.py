# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
# Usando a estrutura WHILE.

contador = ''
inicio = int(input('Digite o Primeiro Termo: '))
razao = int(input('Digite a Razão: '))

while contador > inicio * razao:
    contador = inicio
    contador += razao
    print(contador)