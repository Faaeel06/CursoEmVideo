"""
frase = 'Curso em Vídeo Python'
frase[9::3]
frase[9:13]
frase[9:]
frase[9]
frase[:9]
len(frase)
frase.count('o')
frase.count('o',0,13)
frase.find('deo')
frase.find('Android')
'Curso' in frase
frase.replace('Python', 'Android')
frase.upper()
frase.lower()
frase.capitalize()
frase.title()

frase = '   Aprenda Python  '
frase.strip()
frase.rstrip()
frase.lstrip()

frase = 'Curso em Vídeo Python'
frase.split()
'-'.join(frase)

"""
"""
frase = 'Curso em Vídeo Python'
print(frase)
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])
print(frase.count('o'))
print(frase.upper().count('O'))
print(len(frase))
print(len(frase.strip()))
print(frase.replace('Python', 'Android'))
print(frase.find('Vídeo'))
print(frase.split())
dividido = frase.split()
print(dividido[0])
print(dividido[2][3])
"""