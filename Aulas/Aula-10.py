"""
enquanto não maça:
    passo
pega
while not maça:
    passo
pega

enquanto não maçã:
    se chão:
        passo
    se buraco:
        pula
    se moeda:
        pega
pega
while not maçã:
    if chão:
        passo
    if buraco:
        pula
    if moeda:
        pega
pega
"""

for c in range(1, 10):
    print(c)
print('FIM')

c = 1
while c < 10:
    print(c)
    c += 1
print('FIM')
numero = 1
while numero != 0:
    numero = int(input('Digite um número: '))
print('FIM')

numero = 1
par = impar = 0
while numero != 0:
    numero = int(input('Digite um valor: '))
    if numero != 0:
        if numero % 2 == 0:
            par += 1
        else:
            impar += 1

print(f'Você digitou {par} pares e {impar} ímpares.')
