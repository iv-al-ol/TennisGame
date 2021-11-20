import pygame as pg
import color
import options as opt
import functions as fnc

def map_draw(surf):
    """Рисует карту."""
    def gnd_line(surf):
        """Рисует линию земли."""
        pg.draw.line(surf, color.GREEN, 
                    [opt.WIDTH//100, opt.BALL_LINE], 
                    [opt.WIDTH - opt.WIDTH//100, opt.BALL_LINE], 3)
    def vert_line(surf, pos, t=1):
        """Рисует горизонтальные черточки."""
        pg.draw.line(surf, color.RED, 
                    [pos, opt.BALL_LINE - opt.BALL_LINE//16], 
                    [pos, opt.BALL_LINE + opt.BALL_LINE//16], t)
    
    def draw_vert_lines():
        buff_a = opt.WIDTH//9
        buff_b = buff_a
        for i in range(1, 14, 1):
            buff_b = buff_b + buff_a//i
            vert_line(surf, opt.BORDER - buff_b, 1)
            vert_line(surf, opt.BORDER + buff_b, 1)

    gnd_line(surf)
    vert_line(surf, opt.BORDER, 3)
    #draw_vert_lines()
    
    fnc.draw_text(surf, "Игрок №1", opt.WIDTH//50, 
                  opt.WIDTH//4, opt.HEIGHT//40, color.WHITE)
    fnc.draw_text(surf, "Игрок №2", opt.WIDTH//50, 
                  opt.WIDTH - opt.WIDTH//4, opt.HEIGHT//40, color.WHITE)
    
    fnc.draw_text(surf, "Управление: L-CTRL", opt.WIDTH//60, 
                  opt.WIDTH//4, opt.HEIGHT - opt.HEIGHT//28, color.GRAY)
    fnc.draw_text(surf, "Управление: R-CTRL", opt.WIDTH//60, 
                  opt.WIDTH - opt.WIDTH//4, opt.HEIGHT - opt.HEIGHT//28, color.GRAY)