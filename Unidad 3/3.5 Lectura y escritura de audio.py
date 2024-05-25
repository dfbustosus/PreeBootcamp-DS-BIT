#!python -m pip install -q pygame
# python -m pip install keyboard
import pygame
import keyboard
# inicializar el mixer de Pygame
pygame.mixer.init()

# Cargar el  MP3
pygame.mixer.music.load('ejemplo_mp3.mp3')

# reproducir el MP3
pygame.mixer.music.play()

# Esperar hasta que el MP3 se termine 
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

# Limpiar el objecto Pygame mixer
pygame.mixer.quit()

print('------------------------------------')
# Aqui cuando presiones q no se escuchara nada
pygame.init()

file = 'ejemplo_mp3.mp3'

pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    if keyboard.is_pressed('q'):
        pygame.mixer.music.stop()
        break