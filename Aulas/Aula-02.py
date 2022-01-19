# Tipos Primitivos
'''
Int = 7, -4, 0, 9875...
Float = 4.5, 0,076, -15.223, 7.0...
Bool = True, False
Str = 'Olá', '7.5', ''...
'''

num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))
som = num1 + num2
print('A soma vale', num1 + num2)
print('A soma vale', som)
print('A soma entre {} e {} vale {}'.format(num1, num2, som))
print(type(num1))

num3 = float(input('Digite um valor: '))
print(num3)
print(type(num3))
num3 = bool(input('Digite um valor: '))
print(num3)
print(type(num3))
num3 = int(input('Digite um valor: '))
print(num3)
print(type(num3))
num3 = str(input('Digite um valor: '))
print(num3)
print(type(num3))
print(num3.isnumeric())
print(num3.isalpha())
print(num3.isalnum())
print(num3.isupper())