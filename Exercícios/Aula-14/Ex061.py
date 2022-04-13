# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
# usando a estrutura WHILE.

contador = 0
inicio = int(input('Digite o Primeiro Termo: '))
razao = int(input('Digite a Razão: '))

# for contador in range(inicio, inicio + 10 * razao, razao):
#     print(contador)

while True:
    if contador < (inicio + 10 * razao):
        contador = inicio + razao
    else:
        break
    print(contador)

