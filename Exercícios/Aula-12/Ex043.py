# Desenvolva uma lóogica que leia o peso e a altura de um pessoa, clcule o seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25.0: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida
print(f'{"=" * 20:>}', 'CALCULADORA DE IMC', f'{"=" * 20:>}')

nome = str(input('Digite seu nome: ')).title()
idade = int(input('Digite sua idade: '))
peso = float(input('Digite seu peso atual: '))
altura = int(input('Digite sua altura em cm: '))/100
alerta = ''
condicao = ''
imc = (peso / (altura * altura))

if imc < 18.5:
    condicao = 'Abaixo do peso'
elif 18.5 <= imc < 25.0:
    condicao = 'Peso Ideal'
elif 25.0 <= imc < 30.0:
    condicao = 'Sobrepeso'
    alerta = 'Recomenda-se um acompanhamento médico.'
elif 30.0 <= imc <= 40:
    condicao = 'Obesidadde'
    alerta = 'Procure seu médico.'
else:
    condicao = 'Obesidade Mórbida'
    alerta = 'Procure seu médico com urgência.'
print(f'{"=" * 20:>}', 'RESULTADOS', f'{"=" * 20:>}')
print(f'Paciente: {nome};\n'
      f'Idade: {idade} anos;\n'
      f'IMC: {imc:.2f} Kg/m²\n'
      f'Condição: {condicao}.\n'
      f'{alerta.upper()}')
