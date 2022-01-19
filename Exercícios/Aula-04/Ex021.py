# Faça um programa em python que abra e reproduza o áudio de um arquivo MP3.

import pygame

pygame.init()
pygame.mixer.music.load('Ex021_1.mp3')
pygame.mixer.music.play()
input('está ouvindo?')


from pygame import mixer
mixer.init()
mixer.music.load('Ex021_1.mp3')
mixer.music.play()
input('Agora você escuta?')
