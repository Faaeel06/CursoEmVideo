# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
somatorio = 0
contador = 0
for pares in range(1, 7):
    num = int(input(f'Digite o {pares}° número: '))
    if num % 2 == 0:
        somatorio += num
        contador += 1

print(f'A soma dos {contador} números pares digitados é: {somatorio}')
