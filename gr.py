import pygame

class Ground():
    def __init__(self, screen, speed = -5):
        self.screen = screen
        image = pygame.image.load('sprites/ground.png').convert_alpha()
        rect = pygame.image.load('sprites/ground.png').convert_alpha()
        self.image = pygame.image.load('sprites/ground.png').convert_alpha()
        self.image1 = pygame.image.load('sprites/ground.png').convert_alpha()
        self.rect = image.get_rect()
        self.rect1 = image.get_rect()

        self.rect.bottom = 100
        self.rect1.bottom = 100
        self.rect.x = 0
        self.rect.y = 500
        self.rect1.x = 0
        self.rect1.y = 500
        self.rect1.left = self.rect.right
        self.speed = speed

    def draw(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
        self.screen.blit(self.image1, (self.rect1.x, self.rect1.y))

    def update(self):
        self.rect.left += self.speed
        self.rect1.left += self.speed

        if self.rect.right < 0:
            self.rect.left = self.rect1.right

        if self.rect1.right < 0:
            self.rect1.left = self.rect.right
