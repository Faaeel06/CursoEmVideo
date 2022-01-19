# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

valor = float(input('Digite o valor em metros: '))
print(f'{valor} em metros.\nEquivale a:\n{valor/1000} Km\n{valor/100} Hm\n{valor/10} Dam'
      f'\n{(valor*10):.0f} dm\n{(valor*100):.0f} cm\n{(valor*1000):.0f} mm.')
