#Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras tem o nome completo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

nome = input('Digite seu nome completo: ').strip()
separador = nome.split()
juntos = ''.join(separador)

print(f'O nome digitado em letras maiúsculas foi: {nome.upper()};\n'
      f'O nome digitado em letras minúsculas foi: {nome.lower()};\n'
      f'Ele contêm {len(juntos)} letras;\n'
      f'O primeiro nome contêm {(len(separador[0]))} letras.')
