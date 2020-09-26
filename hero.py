import pygame


class Dinosaur():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('sprites/dino.png').convert_alpha()
        self.img_rect = self.image.get_rect(center=(250, 465))
        self.x = 0

    def update(self, space = False, down = False):
        self.space = space
        self.down = down
        if self.space:
            s = 20
            for i in range(25):

                self.img_rect.y -= s
                s -= 1


    def draw(self):

        self.screen.blit(self.image, self.img_rect,(self.x, 0, 90, 100))
        if self.x > 260:
            self.x = 0
        else:
            self.x += 88
