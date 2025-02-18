from gui import colors, font

font_obj = font.huawenkaiti_font

def draw_score(screen, score):
    text_surface = font_obj.render(f"Score: {score}", True, colors.WHITE)
    text_rect = text_surface.get_rect(topleft=(10, 10))
    screen.blit(text_surface, text_rect)
