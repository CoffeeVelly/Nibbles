import pygame
import main
from gui import colors, font, screen
import sys

pygame.init()

screen.initialize_screen()

try:
    background_image = pygame.image.load("images\startscreen.png")
except pygame.error as message:
    print("Cannot load image: ", message)
    raise SystemExit(message)

background_rect = background_image.get_rect()
SCREEN_WIDTH = background_rect.width
SCREEN_HEIGHT = background_rect.height
pygame.display.set_caption("贪吃蛇-开始界面")

button_width = 200
button_height = 50

# 开始游戏按钮
start_button_x = SCREEN_WIDTH // 2 - button_width // 2
start_button_y = SCREEN_HEIGHT - SCREEN_HEIGHT // 4 - button_height - 20 # 略微调整位置，添加间距
start_button_rect = pygame.Rect(start_button_x, start_button_y, button_width, button_height)

# 退出游戏按钮
exit_button_x = SCREEN_WIDTH // 2 - button_width // 2
exit_button_y = SCREEN_HEIGHT - SCREEN_HEIGHT // 4
exit_button_rect = pygame.Rect(exit_button_x, exit_button_y, button_width, button_height)


def start_screen():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(event.pos):
                    return "start_game"
                elif exit_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    break

        screen.screen.blit(background_image, background_rect)

        # 绘制开始游戏按钮
        pygame.draw.rect(screen.screen, colors.GREEN, start_button_rect)
        start_button_text = font.huawenkaiti_font.render("开始游戏", True, colors.WHITE)
        start_button_text_rect = start_button_text.get_rect(center = start_button_rect.center)
        screen.screen.blit(start_button_text, start_button_text_rect)

        # 绘制退出游戏按钮
        pygame.draw.rect(screen.screen, colors.RED, exit_button_rect)
        exit_button_text = font.huawenkaiti_font.render("退出游戏", True, colors.WHITE)
        exit_button_text_rect = exit_button_text.get_rect(center = exit_button_rect.center)
        screen.screen.blit(exit_button_text, exit_button_text_rect)

        pygame.display.flip()
    return "quit"

# 程序入口点
if __name__ == '__main__':
    while True:
        result = start_screen()
        if result == "start_game":
            main_result = main.main_loop()
            if main_result == "quit":
                break
        else:
            break
    
    pygame.quit()
    sys.exit()