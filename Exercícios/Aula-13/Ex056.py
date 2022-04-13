# Desenvolva um programa que leia o nome, idade e sexo e 4 pessoas. No final do programa mostre:
# - A média de idade do grupo.
# - Qual o nome do homem mais velho.
# - Quantas mulheres têm menos de 20 anos.

total_idade = 0
maioridade_homem = 0
nome_homem_velho = ''
total_mulher_menoridade = 0
for cadastro in range(1, 5):
    print(f'---------- {cadastro}° CADASTRO ----------')
    nome = str(input('Digite seu nome: ')).title()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite seu sexo [M/F]: ')).upper()
    total_idade += idade
    if cadastro == 1 and sexo == 'M':
        maioridade_homem = idade
        nome_homem_velho = nome
    if idade > maioridade_homem and sexo == 'M':
        maioridade_homem = idade
        nome_homem_velho = nome
    if idade < 20 and sexo == 'F':
        total_mulher_menoridade += 1


media_idade = total_idade / 4
print(f'A média de idade do grupo é {media_idade:.2f} anos.\n'
      f'O homem mais velho tem {maioridade_homem} e se chama {nome_homem_velho}.\n'
      f'{total_mulher_menoridade} mulheres tem menos de 20 anos.')
