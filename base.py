import pygame
from pygame.locals import *

pygame.init()

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# xac dinh FPS
FPS = 60
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Animation")

font = pygame.font.SysFont("consolas", 30)
text_surface = font.render("This is a car", True, WHITE, RED)


class Car:
    def __init__(self):
        self.x = 0

        self.surface = pygame.image.load("car.png").convert_alpha()  # xoá phông
        # This code defines a method called "convert_alpha" that takes in a parameter called "surface" of type
        # Surface and returns a value of type Surface.
        # The purpose of this method is to convert the alpha values (transparency) of the pixels on the
        # input surface.

        """
        self.surface = pygame.Surface((100, 50),
                                      SRCALPHA)  # SRCALPHA dùng để xác định đây là 1 surface có đặc tính trong suốt
        pygame.draw.polygon(self.surface, RED, ((15, 0), (65, 0), (85, 15), (100, 15), (100, 40), (0, 40), (0, 15)))
        pygame.draw.circle(self.surface, GREEN, (15, 40), 10)
        pygame.draw.circle(self.surface, GREEN, (85, 40), 10)
        """

    def draw(self):
        DISPLAYSURF.blit(self.surface, (self.x, 100))

    def update(self, move_left, move_right):
        if move_left == True:
            self.x -= 2
        if move_right == True:
            self.x += 2
        if self.x + 100 > WINDOW_WIDTH:
            self.x = WINDOW_WIDTH - 100
        if self.x < 0:
            self.x = 0


        """"
        self.x += 2
        if self.x + 100 > WINDOW_WIDTH:
            self.x = WINDOW_WIDTH - 100
        """


car = Car()
move_left = False
move_right = False
running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            #pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_left = True
            if event.key == pygame.K_RIGHT:
                move_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                move_left = False
            if event.key == pygame.K_RIGHT:
                move_right = False

    DISPLAYSURF.fill(WHITE)
    car.draw()
    car.update(move_left, move_right)

    DISPLAYSURF.blit(text_surface, (50, 10))

    pygame.display.update()
    fpsClock.tick(FPS)
pygame.quit()
