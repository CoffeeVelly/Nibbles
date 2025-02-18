import pygame

pygame.init()
pygame.font.init()

try:
    huawenkaiti_font = pygame.font.Font(r"C:\Windows\Fonts\STKAITI.TTF", 36)
except FileNotFoundError:
    print("Error: Font file not found. Please check the path.")
    huawenkaiti_font = pygame.font.Font(None, 36)  # 使用默认字体作为备选
except pygame.error as e:
    print(f"Error initializing font: {e}")
    huawenkaiti_font = pygame.font.Font(None, 36)  # 使用默认字体作为备选

def get_font():
    return huawenkaiti_font