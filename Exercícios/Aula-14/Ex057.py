# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M" e 'F'. Caso esteja errado, peça a
# digitação novamente até ter um valor correto.

entrada = "Z"
while True:
    if entrada == 'M':
        break
    elif entrada == 'F':
        break
    else:
        entrada = str(input('Digite o sexo [M/F]: ')).upper()
