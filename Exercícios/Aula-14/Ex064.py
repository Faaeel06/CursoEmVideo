# Crie um programa que leia vários números inteiros pelo telcado. o programa só vai parar quando o utilizador digitar o
# valor 999, sendo a condição de parada. No final mostre quantos números foram digitados e qual foi a soma entre
# eles(Desconsiderando o flag).

soma = num = contador = 0

while num != 999:
    num = int(input("Digite um número [Digite 999 para parar]: "))
    soma += num
    contador += 1

print(f"SOMA: {soma-999}", f"Contador: {contador-1}")