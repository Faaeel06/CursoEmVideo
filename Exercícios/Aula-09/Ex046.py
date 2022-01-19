# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifíco, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep

import emoji

for contador in range(10, 0, -1):
    print(contador)
    sleep(1)
for final in range(0, 3):
    print(emoji.emojize(':party_popper:'), emoji.emojize(':party_popper:'), emoji.emojize(':party_popper:'))
    sleep(0.5)
