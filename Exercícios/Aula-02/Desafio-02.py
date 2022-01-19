#Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada

nome = str(input('Digite seu nome completo: '))
dia = int(input('Qual dia você nasceu? '))
mes = str(input('Qual mês você nasceu? '))
ano = int(input('qual ano do seu nascimento? '))

print(f"{nome}, nascida(o) em {dia}/{mes}/{ano}")
