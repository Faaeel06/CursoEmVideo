# Cores no terminal
"""
\033[m
\033['style':'text':'back'm
\033[0:33:44m
Style
0 = nome
1 = bold
4 = underline
7 = negative
Text
30 = white
31 = red
32 = green
33 = yellow
34 = blue
35 = magenta
36 = cian
37 = grey
Back
40 = white
41 = red
42 = green
43 = yellow
44 = blue
45 = magenta
46 = cian
47 = grey
"""
print('\033[0:30:41m Teste \033[m')
print('\033[4:33:44m Teste \033[m')
print('\033[1:35:43m Teste \033[m')
print('\033[0:30:42m Teste \033[m')
print('\033[m Teste \033[m')
print('\033[7:37:40m Teste \033[m')

print('\33[1:31:43mOlá mundo!\33[m')
a = 3
b = 5
c = ['\033[32:41m', '\033[m', '\033[31:44m', '\033[m']
print(f'Os valores são {c[0]}{a}{c[1]} e {c[2]}{b}{c[3]}.')
