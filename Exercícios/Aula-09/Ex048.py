# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3 e que se encontram no intervalo de 1 até 500.
somatorio = 0
contador = 0
for soma in range(1, 501, 2):
    if soma % 3 == 0:
        contador += 1
        somatorio += soma
        print(soma)

print(f'A soma de todos os {contador} números divisíveis por 3 no intervalo de 1 a 500 é {somatorio} ')
