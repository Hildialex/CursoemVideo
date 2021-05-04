import pygame, os
pygame.init()
if os.path.exists('night.mp3'):
    pygame.mixer.music.load('night.mp3')
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(15.5)

    clock = pygame.time.Clock()
    clock.tick(10)

    while pygame.mixer.music.get_busy():
        pygame.event.poll()
        clock.tick(10)
else:
    print('Arquivo não encontrado!')
