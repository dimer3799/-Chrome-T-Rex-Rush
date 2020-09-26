import pygame
from gr import Ground
from hero import Dinosaur
from cact import Cactus


pygame.init()
size_win = (600, 600) # Кортеж с размерами окна

backgound_color = (255 ,255, 255) # Кортеж RGB заднего фона


def run():
    pygame.init()
    gamespeed = 4
    screen = pygame.display.set_mode(size_win)
    screen.fill(backgound_color)
    new_ground = Ground(screen, -1 * gamespeed)
    dino = Dinosaur(screen)
    cactus = Cactus(screen)



    running = True
    while running:
        # Цикл событий
        space = False
        down = False
        for i in pygame.event.get():
            # Закрытие окна на крестик или Alt+F4
            if i.type == pygame.QUIT:
                running = False
            if ((i.type == pygame.KEYDOWN) and (i.key == pygame.K_SPACE)):
                space = True


        screen.fill(backgound_color)
        new_ground.draw()
        new_ground.update()

        dino.update(space, down)
        dino.draw()

        cactus.draw()
        cactus.update(gamespeed)

        pygame.time.delay(40)
        pygame.display.update()





if __name__ == '__main__':
    run()
