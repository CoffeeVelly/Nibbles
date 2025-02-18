import pygame
import random
from gui import colors

class Food:
    def __init__(self, screen_width, screen_height, snake_list):
        self.size = 20 #食物大小
        self.width = screen_width
        self.height = screen_height
        self.snake_list = snake_list
        self.x, self.y = self.generate_food_position() # 初始生成食物

    def generate_food_position(self):
      # 生成食物坐标，避免和蛇身重叠
      while True:
        x = round(random.randrange(0, self.width - self.size) / float(self.size)) * float(self.size)
        y = round(random.randrange(0, self.height - self.size) / float(self.size)) * float(self.size)
        if [x,y] not in self.snake_list: # 避免食物生成在蛇身上
          return x, y

    def draw(self, screen):
        pygame.draw.rect(screen, colors.WHITE, [self.x, self.y, self.size, self.size])

    def respawn(self, snake_list):
      self.snake_list = snake_list
      self.x, self.y = self.generate_food_position()
