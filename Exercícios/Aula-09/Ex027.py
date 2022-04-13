#0Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.
nome = input('Digite seu nome completo: ').strip().split()
print(f'O primeiro nome é {(nome[0]).title()} e seu último nome é {(nome[len(nome)-1]).title()}')


