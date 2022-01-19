# A Confederação Nacional de Natação(CNN) precisa de um programa que leia o ano de nascimento de um atleta e mostre a sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
#  - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima: MASTER
import datetime
print(f'{"=" * 20:>}', 'INFORME DE CLASSE DE ATLETAS', f'{"=" * 20:>}')

nome = str(input("Digite seu nome: "))
nascimento = int(input('Digite o ano do seu nascimento: '))
categoria = ''
idade = datetime.date.today().year - nascimento

if idade <= 9:
    categoria = 'Mirim'
elif idade <= 14:
    categoria = 'Infantil'
elif idade <= 19:
    categoria = 'Júnior'
elif idade <= 25:
    categoria = 'Sênior'
else:
    categoria = 'Master'

print(f'{"=" * 20:>}', 'FICHA DE INSCRIÇÃO', f'{"=" * 20:>}')

print(f'ATLETA: {nome.title()}\n'
      f'IDADE: {idade} anos\n'
      f'CATEGORIA: {categoria}')
