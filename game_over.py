import pygame
from gui import colors, font, screen # 确保正确导入 screen
import sys

def show_game_over_screen(screen_surface, score): # 修改参数名称，更清晰
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button_rect.collidepoint(event.pos):
                    return "restart"
                elif back_to_menu_button_rect.collidepoint(event.pos):
                    return "main_menu"

        screen_width = screen.WIDTH  # 使用全局 screen 的宽度
        screen_height = screen.HEIGHT # 使用全局 screen 的高度

        # 绘制背景
        screen_surface.fill(colors.BLACK)

        # 显示游戏结束文本
        game_over_text = font.huawenkaiti_font.render("游戏结束", True, colors.RED)
        game_over_rect = game_over_text.get_rect(center=(screen_width // 2, screen_height // 4))
        screen_surface.blit(game_over_text, game_over_rect)

        # 显示最终得分
        score_text = font.huawenkaiti_font.render(f"最终得分: {score}", True, colors.WHITE)
        score_rect = score_text.get_rect(center=(screen_width // 2, screen_height // 3))
        screen_surface.blit(score_text, score_rect)

        # 创建重新开始按钮
        button_width = 200
        button_height = 50
        restart_button_x = screen_width // 2 - button_width // 2
        restart_button_y = screen_height // 2
        restart_button_rect = pygame.Rect(restart_button_x, restart_button_y, button_width, button_height)

        # 创建返回主菜单按钮
        back_to_menu_button_x = screen_width // 2 - button_width // 2
        back_to_menu_button_y = screen_height // 2 + button_height + 20  # 略微调整位置，添加间距
        back_to_menu_button_rect = pygame.Rect(back_to_menu_button_x, back_to_menu_button_y, button_width, button_height)

        # 绘制重新开始按钮
        pygame.draw.rect(screen_surface, colors.GREEN, restart_button_rect)
        restart_button_text = font.huawenkaiti_font.render("重新开始", True, colors.WHITE)
        restart_button_text_rect = restart_button_text.get_rect(center=restart_button_rect.center)
        screen_surface.blit(restart_button_text, restart_button_text_rect)

        # 绘制返回主菜单按钮
        pygame.draw.rect(screen_surface, colors.BLUE, back_to_menu_button_rect)
        back_to_menu_text = font.huawenkaiti_font.render("返回主菜单", True, colors.WHITE)
        back_to_menu_text_rect = back_to_menu_text.get_rect(center=back_to_menu_button_rect.center)
        screen_surface.blit(back_to_menu_text, back_to_menu_text_rect)

        pygame.display.flip()

    return "quit"
