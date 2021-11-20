import pygame as pg
from pygame.constants import K_LCTRL

import color
import options as opt
import properties as prop
import functions as fnc

class Ball(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.width = prop.BALL_WIDTH
        self.height = prop.BALL_HEGHT
        self.image = pg.Surface((self.width, self.height))
        self.image.fill(color.YELLOW)
        self.rect = self.image.get_rect()
        self.rect.midtop = (opt.BORDER , opt.HEIGHT//6)
        self.move_speed = prop.BALL_MOVE_SPEED  # Скорость перемещения снаряда
        self.grounded = False  # Приземленное состояние снаряда
        self.direction_move = None  # Направление снаряда
        self.direction_choised = False  # Направление снаряда выбрано
        self.location_area = None  # Зона расположения снаряда

    def update(self):
        def to_land():
            """Приземляет снаряд."""
            self.rect.y += prop.BALL_FALLING_SPEED
            if (self.rect.centery >= opt.BALL_LINE):
                self.rect.centery = opt.BALL_LINE
                self.grounded = True
        
        def choise_direction():
            """Выбирает направление для снаряда."""
            if fnc.random_yes():
                self.direction_move = "Left"
            else:
                self.direction_move = "Right"
            self.direction_choised = True

        def direction():
            """Задает направление движения снаряда."""
            if self.direction_move == "Left":
                self.rect.x -= self.move_speed
            elif self.direction_move == "Right":
                self.rect.x += self.move_speed
        
        if self.grounded == False:
            to_land()
        
        if self.grounded and self.direction_choised == False:
            choise_direction()

        direction()
        
        keystate = pg.key.get_pressed()
        if keystate[pg.K_LCTRL]:
            pass
        if keystate[pg.K_RCTRL]:
            pass

class Base(pg.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pg.sprite.Sprite.__init__(self)
        self.health = prop.BASE_HEALTH  # Здоровье базы
        self.width = prop.BASE_WIDTH
        self.height = prop.BASE_HEGHT * self.health//prop.BASE_HEALTH
        self.image = pg.Surface((self.width, self.height))
        self.image.fill(color.RED)
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)
        
    def update(self, pos_x, pos_y):
        self.width = prop.BASE_WIDTH
        self.height = prop.BASE_HEGHT * self.health//prop.BASE_HEALTH
        self.image = pg.Surface((self.width, self.height))
        self.image.fill(color.RED)
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)