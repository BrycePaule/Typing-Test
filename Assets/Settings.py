import pygame

pygame.font.init()

WORD_LIST_FILEPATH = 'Assets/WORD_LIST.txt'

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
WINDOW_X = (1920 / 2) - (SCREEN_WIDTH / 2)
WINDOW_Y = (1080 / 2) - (SCREEN_HEIGHT / 2)

FPS = 144

BG_COLOR = (215, 175, 255)
INPUT_BOX_COLOR = (230, 205, 255)

# TEXT
FONT = pygame.font.Font('Assets/Fonts/Roboto-Thin.ttf', 16)
# FONT = pygame.font.Font('Assets/Fonts/Roboto-Medium.ttf', 16)
# FONT = pygame.font.Font('Assets/Fonts/Roboto-Bold.ttf', 14)
