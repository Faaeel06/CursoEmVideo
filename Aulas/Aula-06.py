"""
carro.siga()
se carro.esquerda()
    carro.siga()
    carro.direita()
    carro.siga()
    carro.direita()
    carro.siga()
    carro.esquerda()
    carro.siga()
    carro.pare()
senão
    carro.siga()
    carro.esquerda()
    carro.siga()
    carro.esquerda()
    carro.Siga()
"""
"""
carro.siga()
if carro.esquerda():
    carro.siga()
    carro.direita()
    carro.siga()
    carro.direita()
    carro.siga()
    carro.esquerda()
    carro.siga()
    carro.pare()
else:
    carro.siga()
    carro.esquerda()
    carro.siga()
    carro.esquerda()
    carro.Siga()
"""
tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Carro Novo.')
else:
    print('Carro velho.')

print('Carro novo.' if tempo <= 3 else 'Carro velho.')
print('--FIM--')

nome = input('Digite seu nome: ')
if nome == 'Manu':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal.')
print(f'Bom dia, {nome}!')

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota_total = (nota1 + nota2) / 2
print(f'A sua média foi: {nota_total}')
if nota_total >= 6.0:
    print('Sua média foi boa!')
else:
    print('Sua média foi ruim!')
print('Parabéns.' if nota_total >= 6.0 else 'Procure a recuperação.')
