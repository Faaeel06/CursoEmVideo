"""
if carro.esquerda():

elif carro.direita():

elif carro.ré():

else:

"""
comum = ['PEDRO' or 'MARIA' or 'PAULO']
feminino = ['ANA', 'CLÁUDIA', 'JÉSSICA', 'JULIANA']
nome = str(input('Qual é o seu nome? ')).upper()

if nome == 'RAFAEL':
    print('Que nome bonito!')
elif nome == comum:
    print('Seu nome é bem popular no Brasil.')
elif nome in feminino:
    print('Belo nome feminino.')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia, {nome.capitalize()}!')
