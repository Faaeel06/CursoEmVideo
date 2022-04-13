# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando o laço for.
num = int(input('Digite o multiplicando: '))

for tabuada in range(1, 11):
    print(f'{num} *  {tabuada:2} = {(num * tabuada):2}')
