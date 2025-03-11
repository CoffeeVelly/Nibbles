import pygame
from gui import colors, font

class Button:
    def __init__(self, text, x, y, width, height, color, hover_color, action=None, border_radius=15):  # 默认圆角半径
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.hover_color = hover_color
        self.action = action
        self.rect = pygame.Rect(x, y, width, height)
        self.border_radius = border_radius  # 保存圆角半径
        self.is_hovering = False

    def draw(self, screen):
        current_color = self.hover_color if self.is_hovering else self.color
        pygame.draw.rect(screen, current_color, self.rect, border_radius=self.border_radius) # 绘制圆角矩形
        text_surface = font.huawenkaiti_font.render(self.text, True, colors.WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_over(self, pos):
        return self.rect.collidepoint(pos)

    def execute_action(self):
        if self.action:
            return self.action() # 返回 action 的返回值
