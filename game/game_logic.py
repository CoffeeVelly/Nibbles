from gui import screen

SNAKE_SPEED = 1 #游戏速度

def update_game_state(snake_obj, food_obj):
    snake_obj.update() #更新蛇的位置

    #边界检测
    if snake_obj.x >= screen.WIDTH or snake_obj.x < 0 or snake_obj.y >= screen.HEIGHT or snake_obj.y < 0:
      return True  # 游戏结束

    #自撞检测
    if snake_obj.check_collision():
      return True #游戏结束

    #食物检测
    if snake_obj.x == food_obj.x and snake_obj.y == food_obj.y:
      snake_obj.length += 1  #蛇长度增加
      food_obj.respawn(snake_obj.snake_list)  #重新生成食物
    return False  #游戏继续

