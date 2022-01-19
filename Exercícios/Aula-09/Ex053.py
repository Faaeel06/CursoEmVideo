# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
reunir = ''.join(palavras)
reverter = ''
conferir = ''
for palindromo in range(len(reunir) - 1, -1, -1):
    reverter += reunir[palindromo]
print(f'{reunir.title()}\n{reverter.title()}')

if reverter == reunir:
    conferir = 'é PALÍNDROMO'
else:
    conferir = 'não é PALÍNDROMO'

print(f'A frase digitada {conferir}.')
