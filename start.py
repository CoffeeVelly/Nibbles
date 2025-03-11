import pygame
import main
from gui import colors, font, screen, ranking
import sys
from gui.button import Button

pygame.init()  # 确保 Pygame 初始化

screen.initialize_screen()  # 初始化屏幕

try:
    origin_image = pygame.image.load("images\\Nibbles_background.png")
    background_image = pygame.transform.scale(origin_image, (screen.WIDTH, screen.HEIGHT))
except pygame.error as message:
    print("Cannot load image: ", message)
    raise SystemExit(message)

background_rect = background_image.get_rect()
SCREEN_WIDTH = screen.WIDTH # 使用 gui.screen 中定义的宽度
SCREEN_HEIGHT = screen.HEIGHT # 使用 gui.screen 中定义的高度
pygame.display.set_caption("贪吃蛇Mobius")

try:
    icon_path = "images/Mobius.ico"  # 图标文件的路径
    icon = pygame.image.load(icon_path)  # 加载图标，返回 Surface 对象
    pygame.display.set_icon(icon)  # 设置图标
except pygame.error as e:
    print(f"Error loading or setting icon: {e}")

button_width = 200
button_height = 50

# 定义按钮 action
def start_game_action():
    return "start_game"
def ranking_action():
    return "ranking"
def exit_game_action():
    pygame.quit()
    sys.exit()
# 创建按钮实例
start_button = Button(
    "开始游戏",
    880, 180,  # x, y
    button_width, button_height,
    colors.SKY_BLUE, colors.LIGHT_SKY_BLUE,  # 颜色，悬停颜色
    action=start_game_action
)
ranking_button = Button(
    "排行榜",
    880, 180 + button_height + 10,  # x, y
    button_width, button_height,
    colors.PALE_GOLD, colors.ACIENT_WHITE, # 颜色，悬停颜色
    action=ranking_action
)
exit_button = Button(
    "退出游戏",
    880, 180 + button_height * 2 + 20,  # x, y
    button_width, button_height,
    colors.CYAN, colors.TEAL,  # 颜色，悬停颜色
    action=exit_game_action
)


def start_screen(restart):
    if restart == True:
        return "start_game"
    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit() #在退出前正确关闭 Pygame
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.is_over(mouse_pos):
                    return start_button.execute_action()
                elif ranking_button.is_over(mouse_pos):
                    return ranking_button.execute_action()
                elif exit_button.is_over(mouse_pos):
                    exit_button.execute_action()  # Exit action doesn't need return
            # 悬停事件处理
            if event.type == pygame.MOUSEMOTION:
                start_button.is_hovering = start_button.is_over(mouse_pos)
                ranking_button.is_hovering = ranking_button.is_over(mouse_pos)
                exit_button.is_hovering = exit_button.is_over(mouse_pos)

        screen.screen.blit(background_image, background_rect)

        start_button.draw(screen.screen)
        ranking_button.draw(screen.screen)
        exit_button.draw(screen.screen)

        pygame.display.flip()
    return "quit"

# 程序入口点
if __name__ == '__main__':
    file_path = 'user_data/score.json'
    scores = ranking.load_scores(file_path)
    restart = False
    while True:
        result = start_screen(restart)
        restart = False
        if result == "start_game":
            main_result = main.main_loop()
            if main_result == "quit":
                break
            elif main_result == "main_menu": #处理返回主菜单的情况
                continue
            elif main_result == "restart":
                restart = True
                continue
        elif result == "ranking":
            ranking.display_scores()
        else:
            break
    
    pygame.quit()
    sys.exit()