import pygame


class Cactus():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('sprites/cacti-small.png').convert_alpha()
        self.img_rect = self.image.get_rect(center=(550, 472))

    def update(self, speed):
        self.img_rect.x -= speed




    def draw(self):
        self.screen.blit(self.image, self.img_rect,(0, 0, 34, 70))
