import json
import pygame
import os
from game import update_score
from gui import screen, colors, font

def load_scores(file_path):
    if not os.path.exists(file_path):
        return []
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def get_top_scores(scores, top_n=10):
    sorted_scores = sorted(scores, key=lambda x: x['score'], reverse=True)
    return sorted_scores[:top_n]

def display_scores():
    file_path = 'user_data/score.json'
    scores = load_scores(file_path)
    top_scores = get_top_scores(scores)

    background_image = pygame.image.load("images/ranking_background.png").convert()
    background_image.set_colorkey((0, 0, 0))
    background_rect = background_image.get_rect()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return "quit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    return "main_menu"

        screen.screen.blit(background_image, background_rect) # 绘制背景



        # 绘制标题
        title_text = font.huawenkaiti_font.render("排行榜", True, colors.PURPLE)
        title_rect = title_text.get_rect(center=(screen.WIDTH // 2, 50))
        screen.screen.blit(title_text, title_rect)

        # 显示排行榜条目
        y_offset = 120  # 起始 Y 坐标
        for i, score_data in enumerate(top_scores):
            name = score_data['name']
            score = score_data['score']
            entry_text = font.huawenkaiti_font.render(f"{i+1}. {name}: {score}", True, colors.PURPLE)
            entry_rect = entry_text.get_rect(center=(screen.WIDTH // 2, y_offset))
            screen.screen.blit(entry_text, entry_rect)
            y_offset += 40

        pygame.display.flip()
    

def input_player_name(score):
    player_name = ""
    inputting = True
    background_image = pygame.image.load("images/ranking_background.png").convert()
    background_image.set_colorkey((0, 0, 0))
    background_rect = background_image.get_rect()

    while inputting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None  # 玩家退出游戏
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    inputting = False
                elif event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]
                else:
                    player_name += event.unicode

        screen.screen.blit(background_image, background_rect)

        # 绘制文本输入提示
        prompt_text = font.huawenkaiti_font.render("请输入你的名字:", True, colors.PURPLE)
        prompt_rect = prompt_text.get_rect(center=(screen.WIDTH // 2, screen.HEIGHT // 2 - 40))
        screen.screen.blit(prompt_text, prompt_rect)

        # 绘制文本输入框
        input_box_rect = pygame.Rect(screen.WIDTH // 2 - 100, screen.HEIGHT // 2 - 10, 200, 40)
        pygame.draw.rect(screen.screen, colors.PURPLE, input_box_rect, 2)

        # 绘制输入的文本
        name_text = font.huawenkaiti_font.render(player_name, True, colors.PURPLE)
        name_rect = name_text.get_rect(center=input_box_rect.center)
        screen.screen.blit(name_text, name_rect)

        pygame.display.flip()

    if player_name:
        if player_name == "":
            player_name = "匿名"
        update_score.record_score(player_name, score)