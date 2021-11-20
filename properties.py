import options as opt

# Ball properties
BALL_HEGHT = opt.HEIGHT//18  # Высота снаряда
BALL_WIDTH = opt.WIDTH//32  # Ширина снаряда
BALL_FALLING_SPEED = 5  # Скорость падения снаряда
BALL_MOVE_SPEED = 20  # Скорость передвижения снаряда

# Base properties
BASE_HEGHT = opt.HEIGHT//2  # Высота базы
BASE_WIDTH = opt.WIDTH//24  # Ширина базы
BASE_HEALTH = 100  # Прочность базы
BASE_1_COORD = (opt.WIDTH//40, opt.BALL_LINE)  # Координаты первой базы
BASE_2_COORD = (opt.WIDTH - opt.WIDTH//40, opt.BALL_LINE)  # Координаты второй базы

# Players properties
PLAYER_1_SCORE = 0  # Очки первого игрока
PLAYER_2_SCORE = 0  # Очки второго игрока