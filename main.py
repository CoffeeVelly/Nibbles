import pygame
from game import game_logic, snake, food
from gui import screen, text
import game_over as game_over
import sys

# Snake 和 Food 对象 (全局变量)
snake_obj = None
food_obj = None

def initialize_game():
    """初始化游戏状态，创建新的 Snake 和 Food 对象."""
    global snake_obj, food_obj
    snake_obj = snake.Snake()
    food_obj = food.Food(screen.WIDTH, screen.HEIGHT, snake_obj.snake_list)

# 游戏主循环
def main_loop():
    global snake_obj, food_obj

    initialize_game()  # 在每次开始游戏时调用

    clock = pygame.time.Clock()
    game_over_flag = False

    while not game_over_flag:
        # 处理事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit" # 退出游戏
            snake_obj.handle_input(event)

        # 游戏逻辑
        if game_logic.update_game_state(snake_obj, food_obj):
            # 如果发生碰撞或超出边界，游戏结束
            game_over_flag = True

        # 绘制游戏
        screen.draw_background()
        food_obj.draw(screen.screen)
        snake_obj.draw(screen.screen)
        text.draw_score(screen.screen, snake_obj.length - 1)  # 显示得分

        pygame.display.update()
        clock.tick(game_logic.SNAKE_SPEED)

    # 游戏结束，显示游戏结束画面
    result = game_over.show_game_over_screen(screen.screen, snake_obj.length - 1)
    return result
