import options as opt

# Ball properties
BALL_HEGHT = opt.HEIGHT//18  # Высота снаряда
BALL_WIDTH = opt.WIDTH//32  # Ширина снаряда
BALL_FALLING_SPEED = 5  # Скорость падения снаряда
BALL_START_SPEED = 5  # Скорость передвижения снаряда
BALL_FAIL_SPEED_UP = 3
BALL_BEST_SPEED_UP = 5

# Base properties
BASE_HEGHT = opt.HEIGHT//2  # Высота базы
BASE_WIDTH = opt.WIDTH//24  # Ширина базы
BASE_HEALTH = 100  # Прочность базы
BASE_1_COORD = (opt.WIDTH//40, opt.BALL_LINE)  # Координаты первой базы
BASE_2_COORD = (opt.WIDTH - opt.WIDTH//40, opt.BALL_LINE)  # Координаты второй базы

# Players properties
PLAYER_1_SCORE = 0  # Очки первого игрока
PLAYER_2_SCORE = 0  # Очки второго игрока
PLAYER_1_KEY_PRESSED = False
PLAYER_2_KEY_PRESSED = False
