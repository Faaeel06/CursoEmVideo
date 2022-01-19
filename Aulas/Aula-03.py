'''
5+2 == 7
5-2 == 3
5*2 == 10
5/2 == 2.5
5**2 == 25
5//2 == 2
5%2 == 1
'''

'''
1° ()
2° **
3° * ; / ; // ; %
4° + ; - 
'''

'''
5+3*2 == 11
3*5+4**2 == 31
3*(5+4)**2 == 243
'''
'''
nome = input('Qual o seu nome? ')
print(f'prazer em te conhecer {nome:=^20}!')
'''
num1 = int(input('Um valor: '))
num2 = int(input('Outro valor: '))
print(f'A soma vale {num1+num2}.', end=' ')
print(f'A multiplicação vale {num1*num2}.', end=' ')
print(f'A divisão vale {num1/num2:.3f}.', end=' ')
print(f'A parte inteira da divisão inteira vale {num1//num2}.', end=' ')
print(f'A exponenciação vale {num1**num2}.', end=' ')
