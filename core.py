import pygame as pg

import color
import space
import options as opt
import objects as obj
import functions as fnc
import properties as prop

pg.init()  # Инициализируется окно программы
screen = pg.display.set_mode([opt.WIDTH, opt.HEIGHT])  # Задаются размеры окна
pg.display.set_caption("Простой теннис")  # Задается название в шапке окна
clock = pg.time.Clock()  # Задаются внутренние часы программы

# Создаются группы спрайтов
all_sprites = pg.sprite.Group()  

def create_ball():
    """Создает снаряд."""
    ball = obj.Ball()
    all_sprites.add(ball)
    return ball
    
def create_base(coord):
    """Создает базу."""
    base = obj.Base(coord)
    all_sprites.add(base)
    return base

# Создаются объекты
game_ball = create_ball()
base_plr_1 = create_base(prop.BASE_1_COORD)
base_plr_2 = create_base(prop.BASE_2_COORD)

running = True
while running:
    clock.tick(opt.FPS)  # Контроль частоты кадров
    
    # Проверка событий
    for event in pg.event.get():  
        if event.type == pg.QUIT:
            running = False
    
    # Контроль столкновений
    if pg.sprite.collide_rect(game_ball, base_plr_1):
        game_ball.direction_move = "Right"
        base_plr_1.health -= game_ball.move_speed
        base_plr_1.update(prop.BASE_1_COORD)
    if pg.sprite.collide_rect(game_ball, base_plr_2):
        game_ball.direction_move = "Left"
        base_plr_2.health -= game_ball.move_speed
        base_plr_2.update(prop.BASE_2_COORD)
    
    if not game_ball.alive():
        game_ball = create_ball()
        base_plr_1.kill()
        base_plr_2.kill()
        base_plr_1 = create_base(prop.BASE_1_COORD)
        base_plr_2 = create_base(prop.BASE_2_COORD)
    
    game_ball.update()  # Обновление спрайтов

    screen.fill(color.BLACK)  # Заливка фона черным цветом

    space.map_draw(screen)  # Отрисовка элементов игрового пространства

    all_sprites.draw(screen)  # Отрисовка спрайтов
    
    # Отображение очков
    fnc.draw_text(screen, str(prop.PLAYER_1_SCORE), opt.HEIGHT//20,
                  opt.WIDTH//4, opt.HEIGHT//10, color.BLUE)
    fnc.draw_text(screen, str(prop.PLAYER_2_SCORE), opt.HEIGHT//20,
                  opt.WIDTH - opt.WIDTH//4, opt.HEIGHT//10, color.BLUE)
    
    pg.display.flip()  # Смена кадра дисплея
pg.quit()
