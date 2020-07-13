import pygame
from Constants import *

###############################################
# Button()
###############################################

class Button():
    __x = 0
    __y = 0
    __width = 0
    __height = 0
    __label = ""

    def __init__(self, x, y, width, height, label):
        self.__x = int(x)
        self.__y = int(y)
        self.__width = int(width)
        self.__height = int(height)
        self.__label = label

    def draw(self, screen):
        pygame.draw.rect(screen, BUTTON_BORDER_COLOR, (self.__x, self.__y, self.__width, self.__height), 0)        
        pygame.draw.rect(screen, BUTTON_COLOR, (self.__x + BUTTON_BORDER_SIZE, self.__y + BUTTON_BORDER_SIZE, self.__width - (BUTTON_BORDER_SIZE * 2), self.__height - (BUTTON_BORDER_SIZE * 2)), 0)

        label_font = pygame.font.SysFont('courier', BUTTON_FONT_SIZE, bold = True)
        label_text = label_font.render(self.__label, 1, BUTTON_LABEL_COLOR)
        label_x = ((self.__width / 2) - (label_text.get_width() / 2) + self.__x)
        label_y = ((self.__height / 2) - (label_text.get_height() / 2) + self.__y)
        screen.blit(label_text, (int(label_x), int(label_y)))

    def is_over(self, mouse_x, mouse_y):
        return ((mouse_x >= self.__x) and (mouse_x < (self.__x + self.__width)) and (mouse_y >= self.__y) and (mouse_y < (self.__y + self.__height)))