# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
#de tintas necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²

altura = float(input('Digite a altura da parede(Em metros): '))
largura = float(input('Digite a largura da parede(Em metros): '))

print(f'A área total da parede é: {altura*largura}.\nPara pintá-la será necessário {(altura*largura)/2}L de tinta.')