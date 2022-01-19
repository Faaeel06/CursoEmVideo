"""
laço c no intervalo(1, 10):
    passo
passo
"""
"""
for c in range(1, 10):
    passo
passo
"""

for c in range(0, 6):
    print('Oi')
print('FIM')

for c in range(0, 7):
    print(c)
print('FIM')

for c in range(6, 0, -1):
    print(c)
print('FIM')

for c in range(0, 7, 2):
    print(c)
print('FIM')

num = int(input('Digite um número: '))
for c in range(0, num+1):
    print(c)
print('FIM')

inicio = int(input('Início: '))
final = int(input('Fim: '))
passo = int(input('Intervalo: '))

for contando in range(inicio, final + 1, passo):
    print(contando)
print('FIM...')

for c in range(0, 3):
    numero = int(input('Digite um valor: '))
print('Fim')

somatorio = 0
for c in range(0, 4):
    numero = int(input('Digite um valor: '))
    somatorio += numero
print(f'O somatório de todos so valores foi {somatorio}')
