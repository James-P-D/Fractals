import pygame # Tested with pygame v1.9.6
import numpy as np
from Constants import *
from UIControls import *

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

mandlebrot_button = Button((LARGE_BUTTON_WIDTH * 0), BUTTON_STRIP_TOP, LARGE_BUTTON_WIDTH, LARGE_BUTTON_HEIGHT, MANDLEBROT_BUTTON_LABEL)
zoom_button = Button((LARGE_BUTTON_WIDTH * 1), BUTTON_STRIP_TOP, LARGE_BUTTON_WIDTH, LARGE_BUTTON_HEIGHT, ZOOM_DEFAULT_BUTTON_LABEL)
inc_zoom_button = Button((SMALL_BUTTON_WIDTH * 0) + (LARGE_BUTTON_WIDTH * TOTAL_LARGE_BUTTONS), BUTTON_STRIP_TOP, SMALL_BUTTON_WIDTH, SMALL_BUTTON_HEIGHT, ZOOM_INC_BUTTON_LABEL)
dec_zoom_button = Button((SMALL_BUTTON_WIDTH * 1) + (LARGE_BUTTON_WIDTH * TOTAL_LARGE_BUTTONS), BUTTON_STRIP_TOP, SMALL_BUTTON_WIDTH, SMALL_BUTTON_HEIGHT, ZOOM_DEC_BUTTON_LABEL)

###############################################
# game_loop()
###############################################

def game_loop():
    game_exit = False
    clock = pygame.time.Clock()
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True;
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass

        pygame.display.update()
        clock.tick(CLOCK_TICK)
    pygame.quit()

###############################################
# draw_ui()
###############################################

def draw_ui():
    screen.fill(BLACK)
    mandlebrot_button.draw(screen)
    zoom_button.draw(screen)
    inc_zoom_button.draw(screen)
    dec_zoom_button.draw(screen)
    

###############################################
# main()
###############################################

def main():
    pygame.init()

    draw_ui()

    game_loop()

###############################################
# Startup
###############################################

if __name__ == "__main__":
    main()

