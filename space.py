import pygame as pg
import color
import options as opt

def map_draw(scrn):
    """Рисует карту."""
    def gnd_line(scrn):
        """Рисует линию земли."""
        pg.draw.line(scrn, color.GREEN, [opt.WIDTH//100, opt.BALL_LINE], 
                            [opt.WIDTH - opt.WIDTH//100, opt.BALL_LINE], 3)
    def vert_line(scrn, pos, t=1):
        """Рисует горизонтальные черточки."""
        pg.draw.line(scrn, color.RED, [pos, opt.BALL_LINE - opt.BALL_LINE//16], 
                            [pos, opt.BALL_LINE + opt.BALL_LINE//16], t)
    
    def draw_vert_lines():
        buff_a = opt.WIDTH//9
        buff_b = buff_a
        for i in range(1, 14, 1):
            buff_b = buff_b + buff_a//i
            vert_line(scrn, opt.BORDER - buff_b, 1)
            vert_line(scrn, opt.BORDER + buff_b, 1)

    gnd_line(scrn)
    vert_line(scrn, opt.BORDER, 3)
    draw_vert_lines()
    