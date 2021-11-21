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
        self.owner = None  # Принадлежность к игроку
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
        
        def check_death_border():
            """Проверяет пересечение границы смерти."""
            if (self.rect.centerx <= opt.DEATH_LINE_1):
                prop.PLAYER_2_SCORE += 1
                self.kill()
            if (self.rect.centerx >= opt.DEATH_LINE_2):
                prop.PLAYER_1_SCORE += 1
                self.kill()
        
        def arrival():
            """Условие приземления и выбора направления."""
            if not self.grounded:
                to_land()
            if self.grounded and not self.direction_choised:
                choise_direction()
        
        def check_location():
            """Проверяет расположение снаряда."""
            if self.rect.right < opt.BORDER:
                self.owner = 1
                if self.rect.right > opt.WIDTH * 2/6:
                    self.location_area = "Fail_1"
                elif self.rect.right > opt.WIDTH * 1/6:
                    self.location_area = "Normal_1"
                elif self.rect.right > 0:
                    self.location_area = "Best_1"
            elif self.rect.left > opt.BORDER:
                self.owner = 2
                if self.rect.left < opt.WIDTH * 4/6:
                    self.location_area = "Fail_2"
                elif self.rect.left < opt.WIDTH * 5/6:
                    self.location_area = "Normal_2"
                elif self.rect.left < opt.WIDTH:
                    self.location_area = "Best_2"
            else:
                self.owner = None
            
        def control():
            """Отвечает за управление направлением снаряда."""
            keystate = pg.key.get_pressed()
            if self.owner == 1:
                if keystate[pg.K_LCTRL]:
                    self.direction_move = "Right"
            if self.owner == 2:
                if keystate[pg.K_RCTRL]:
                    self.direction_move = "Left"
        
        arrival()
        direction()
        check_location()
        control()
        check_death_border()

class Base(pg.sprite.Sprite):
    def __init__(self, coord):
        pg.sprite.Sprite.__init__(self)
        self.health = prop.BASE_HEALTH  # Здоровье базы
        self.width = prop.BASE_WIDTH
        self.height = prop.BASE_HEGHT * self.health//prop.BASE_HEALTH
        self.image = pg.Surface((self.width, self.height))
        self.image.fill(color.RED)
        self.rect = self.image.get_rect()
        self.rect.center = (coord)
        
    def update(self, coord):
        self.width = prop.BASE_WIDTH
        self.height = prop.BASE_HEGHT * self.health//prop.BASE_HEALTH
        self.image = pg.Surface((self.width, self.height))
        self.image.fill(color.RED)
        self.rect = self.image.get_rect()
        self.rect.center = (coord)
