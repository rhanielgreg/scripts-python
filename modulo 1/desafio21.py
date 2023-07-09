#faca um progama em python que abra e reproduza o audio de um aquivo mp3
#colocar arquivo mp3 na mesma pasta
import pygame

pygame.init()

pygame.mixer.music.load('nokia.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()

