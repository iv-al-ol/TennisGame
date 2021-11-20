import pygame as pg

import color
import space
import options as opt
import objects as obj
import functions as fnc
import properties as prp

pg.init()  # Инициализируется окно программы
screen = pg.display.set_mode([opt.WIDTH, opt.HEIGHT])  # Задаются размеры окна
pg.display.set_caption("Простой теннис")  # Задается название в шапке окна
clock = pg.time.Clock()  # Задаются внутренние часы программы

# Создаются группы спрайтов
all_sprites = pg.sprite.Group()  
base_sprites = pg.sprite.Group()
ball_sprites = pg.sprite.Group()

# Создаются объекты
game_ball = obj.Ball()
base_plr_1 = obj.Base(opt.WIDTH//40, opt.BALL_LINE)
base_plr_2 = obj.Base(opt.WIDTH - opt.WIDTH//40, opt.BALL_LINE)

# Объекты добавляются в группу
all_sprites.add(game_ball, base_plr_1, base_plr_2)  
base_sprites.add(base_plr_1, base_plr_2)

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
        base_plr_1.update(opt.WIDTH//40, opt.BALL_LINE)
    if pg.sprite.collide_rect(game_ball, base_plr_2):
        game_ball.direction_move = "Left"
        base_plr_2.health -= game_ball.move_speed
        base_plr_2.update(opt.WIDTH - opt.WIDTH//40, opt.BALL_LINE)
    
    game_ball.update()  # Обновление спрайтов

    screen.fill(color.BLACK)  # Заливка фона черным цветом

    space.map_draw(screen)  # Отрисовка элементов игрового пространства

    all_sprites.draw(screen)  # Отрисовка спрайтов
    
    # Отображение очков
    fnc.draw_text(screen, str(prp.PLAYER_1_SCORE), opt.HEIGHT//20,
                  opt.WIDTH//4, opt.HEIGHT//10, color.BLUE)
    fnc.draw_text(screen, str(prp.PLAYER_2_SCORE), opt.HEIGHT//20,
                  opt.WIDTH - opt.WIDTH//4, opt.HEIGHT//10, color.BLUE)
    
    pg.display.flip()  # Смена кадра дисплея
pg.quit()
