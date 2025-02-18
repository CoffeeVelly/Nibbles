import pygame
from gui import colors

WIDTH = 854
HEIGHT = 460

screen = None 

def initialize_screen():
  global screen
  screen = pygame.display.set_mode((WIDTH, HEIGHT))
  pygame.display.set_caption("贪吃蛇")


def draw_background():
    screen.fill(colors.BLACK)
