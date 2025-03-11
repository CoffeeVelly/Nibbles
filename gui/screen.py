import pygame
from gui import colors

WIDTH = 1200
HEIGHT = 800

screen = None 

def initialize_screen():
  global screen
  pygame.init()
  screen = pygame.display.set_mode((WIDTH, HEIGHT))
  pygame.display.set_caption("贪吃蛇")
  screen.fill(colors.BLACK)
  pygame.display.flip()

def get_width():
    return WIDTH

def get_height():
    return HEIGHT