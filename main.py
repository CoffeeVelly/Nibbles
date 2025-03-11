import pygame
from game import game_logic, snake, food
from gui import screen, text, ranking
import game_over as game_over
from game import update_score

# Snake 和 Food 对象 (全局变量)
snake_obj = None
food_obj = None

def initialize_game():
    global snake_obj, food_obj
    snake_obj = snake.Snake()
    food_obj = food.Food(screen.WIDTH, screen.HEIGHT, snake_obj.snake_list)

# 游戏主循环
def main_loop():
    global snake_obj, food_obj

    initialize_game()  # 在每次开始游戏时调用

    clock = pygame.time.Clock()
    game_over_flag = False
    origin_image = pygame.image.load("images/nifu.png").convert_alpha()
    background_image = pygame.transform.scale(origin_image, (screen.WIDTH, screen.HEIGHT))
    mask_surface = pygame.Surface(background_image.get_size(), pygame.SRCALPHA)
    mask_alpha = 128
    mask_surface.fill((0, 0, 0, mask_alpha))
    
    
    background_rect = background_image.get_rect()

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
        
        screen.screen.blit(background_image, background_rect)
        screen.screen.blit(mask_surface, background_rect)
        food_obj.draw(screen.screen)
        snake_obj.draw(screen.screen)
        text.draw_score(screen.screen, snake_obj.length - 1)  # 显示得分

        pygame.display.update()
        clock.tick(30)

    # 游戏结束，显示游戏结束画面
    ranking.input_player_name(snake_obj.length - 1)
    result = game_over.show_game_over_screen(screen.screen, snake_obj.length - 1) # 传递 screen.screen
    return result
