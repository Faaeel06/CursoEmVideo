#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = input('Digite uma frase: ').upper().strip()
print(f"Na frase digitada a letra A aparece {frase.count('A')} vezes")
print(f"a primeira vez que apareceu a letra A foi {frase.find('A')+1} e a última vez foi {frase.rfind('A')+1}")
