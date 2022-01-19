# Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite o valor atual do salário: R$ '))

if salario > 1250.00:
    aumento = salario + (salario * 0.10)
    print(f'Seu salário foi reajustado em 10%, o novo valor é: R${aumento:.2f}')
else:
    aumento = salario + (salario * 0.15)
    print(f'Seu salário foi reajustado em 15%, o novo valor é: R${aumento:.2f}')
