# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: Todos os lados iguais
# - ISÓCELES: dois lados iguais
# - ESCALENO: Todos os lados diferentes
print(f'{"=" * 20:>}', 'CATEGORIA DE TRIÂNGULOS', f'{"=" * 20:>}')

lado_a = float(input('Digite a extensão da primeira reta: '))
lado_b = float(input('Digite a extensão da segunda reta: '))
lado_c = float(input('Digite a extensão da terceira reta: '))

if lado_a < lado_b + lado_c and lado_b < lado_a + lado_c and lado_c < lado_a + lado_b:
    print('Pode formar um triângulo.')
    if lado_a == lado_b == lado_c:
        print('Este é um triângulo EQUILÁTERO.')
    elif lado_a == lado_b != lado_c or lado_c == lado_a != lado_b or lado_c == lado_b != lado_a:
        print('Este é um triângulo ISÓCELES.')
    elif lado_a != lado_b != lado_c != lado_a:
        print('Este é um triângulo ESCALENO.')
else:
    print('Essas retas não podem formar um triângulo.')
