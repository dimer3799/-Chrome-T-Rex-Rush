import pygame

height = 400
width = 10
pygame.rect.bottom = int(0.98*height)
pygame.rect.left = width/15


class Dinosaur():
    def __init__(self, screen):
        self.screen = screen
        
