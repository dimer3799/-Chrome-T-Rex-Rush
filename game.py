import pygame
from gr import Ground

pygame.init()
size_win = (600, 600) # Кортеж с размерами окна

backgound_color = (255 ,255, 255) # Кортеж RGB заднего фона


def run():
    pygame.init()
    gamespeed = 4
    screen = pygame.display.set_mode(size_win)
    screen.fill(backgound_color)
    new_ground = Ground(screen, -1 * gamespeed)



    running = True
    while running:
        # Цикл событий
        for i in pygame.event.get():
            # Закрытие окна на крестик или Alt+F4
            if i.type == pygame.QUIT:
                running = False

        new_ground.draw()
        #new_ground.update()
        #pygame.time.delay(20)
        pygame.display.update()





if __name__ == '__main__':
    run()
