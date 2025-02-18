import pygame
from gui import colors

class Snake:
    def __init__(self):
        self.x = 300  # 初始位置
        self.y = 240
        self.x_change = 0
        self.y_change = 0
        self.snake_list = []
        self.length = 1
        self.block_size = 20 #蛇身块大小

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and self.x_change != self.block_size:
                self.x_change = -self.block_size
                self.y_change = 0
            elif event.key == pygame.K_RIGHT and self.x_change != -self.block_size:
                self.x_change = self.block_size
                self.y_change = 0
            elif event.key == pygame.K_UP and self.y_change != self.block_size:
                self.y_change = -self.block_size
                self.x_change = 0
            elif event.key == pygame.K_DOWN and self.y_change != -self.block_size:
                self.y_change = self.block_size
                self.x_change = 0


    def update(self):
        self.x += self.x_change
        self.y += self.y_change
        snake_head = [self.x, self.y]
        self.snake_list.append(snake_head)

        if len(self.snake_list) > self.length:
            del self.snake_list[0]

    def draw(self, screen):
        for x in self.snake_list:
            pygame.draw.rect(screen, colors.GREEN, [x[0], x[1], self.block_size, self.block_size])

    def check_collision(self):
        # 检查与自身的碰撞
        for x in self.snake_list[:-1]:
            if x == self.snake_list[-1]:  # 蛇头和身体碰撞
                return True
        return False
