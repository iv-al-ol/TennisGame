import pygame as pg

import color
import options as opt
import objects as obj
import space
import functions as fnc

pg.init()

screen = pg.display.set_mode([opt.WIDTH, opt.HEIGHT])
pg.display.set_caption("GAME")
clock = pg.time.Clock()

all_sprites = pg.sprite.Group()
upd_sprites = pg.sprite.Group()
game_ball = obj.Ball()
base_plr_1 = obj.Base(opt.WIDTH//40, opt.HEIGHT//2)
base_plr_2 = obj.Base(opt.WIDTH - opt.WIDTH//40, opt.HEIGHT//2)
all_sprites.add(game_ball, base_plr_1, base_plr_2)
upd_sprites.add(game_ball)

running = True
while running:
    
    clock.tick(opt.FPS)
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    if pg.sprite.collide_rect(game_ball, base_plr_1):
        game_ball.direction_move = "Right"
    if pg.sprite.collide_rect(game_ball, base_plr_2):
        game_ball.direction_move = "Left"
    
    upd_sprites.update()

    screen.fill(color.BLACK)

    space.map_draw(screen)

    all_sprites.draw(screen) 

    pg.display.flip()

pg.quit()
