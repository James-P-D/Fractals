import pygame # Tested with pygame v1.9.6
import numpy as np
from Constants import *
from UIControls import *

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

zoom_steps = MIN_ZOOM_STEPS

mandlebrot_button = Button((LARGE_BUTTON_WIDTH * 0), BUTTON_STRIP_TOP, LARGE_BUTTON_WIDTH, LARGE_BUTTON_HEIGHT, MANDLEBROT_BUTTON_LABEL)
zoom_button = Button((LARGE_BUTTON_WIDTH * 1), BUTTON_STRIP_TOP, LARGE_BUTTON_WIDTH, LARGE_BUTTON_HEIGHT, ZOOM_BUTTON_LABEL.format(zoom_steps))
inc_zoom_button = Button((SMALL_BUTTON_WIDTH * 0) + (LARGE_BUTTON_WIDTH * TOTAL_LARGE_BUTTONS), BUTTON_STRIP_TOP, SMALL_BUTTON_WIDTH, SMALL_BUTTON_HEIGHT, ZOOM_INC_BUTTON_LABEL)
dec_zoom_button = Button((SMALL_BUTTON_WIDTH * 1) + (LARGE_BUTTON_WIDTH * TOTAL_LARGE_BUTTONS), BUTTON_STRIP_TOP, SMALL_BUTTON_WIDTH, SMALL_BUTTON_HEIGHT, ZOOM_DEC_BUTTON_LABEL)


###############################################
# game_loop()
###############################################

def game_loop():
    
    def flip_rect(x1, x2, y1, y2, x_inc, y_inc):
        
        def flip_pixel(x, y):
            (r, g, b, a) = screen.get_at((x, y))
            screen.set_at((x, y), (255-r, 255-g, 255-b, a))

        for x in range(x1, x2, x_inc):
            flip_pixel(x, y1)
            flip_pixel(x, y2)
        for y in range(y1, y2, y_inc):
            flip_pixel(x1, y)
            flip_pixel(x2, y)


    game_exit = False
    clock = pygame.time.Clock()

    selecting_zoom_area = False
    (x1, y1, x2, y2) = (-1, -1, -1, -1)

    while not game_exit:
        pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True;
            elif (event.type == pygame.MOUSEMOTION) and (selecting_zoom_area) :    
                # Flip the existing rectangle to remove it
                flip_rect(x1, x2, y1, y2, 1 if x1 < x2 else -1, 1 if y1 < y2 else -1)                
                # Get the new (x2, y2) corner
                (x2, y2) = pygame.mouse.get_pos()
                # Make sure y2 is no lower than the bottom of the canvas
                y2 = min(CANVAS_HEIGHT - 1, y2)
                # Draw the new rectangle with a new (x2, y2) corner
                flip_rect(x1, x2, y1, y2, 1 if x1 < x2 else -1, 1 if y1 < y2 else -1)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                (mouse_x, mouse_y) = pygame.mouse.get_pos()
                if (mouse_y < CANVAS_HEIGHT):
                    # If x1, y1, x2, y2 are all -1, then we have already drawn an rectangle on screen
                    # Draw it again to overwrite it before we draw a new one
                    if (x1 != -1) and (x2 != -1) and (y1 != -1) and (y2 != -1):
                        flip_rect(x1, x2, y1, y2, 1 if x1 < x2 else -1, 1 if y1 < y2 else -1)
                
                    x1 = x2 = mouse_x
                    y1 = y2 = mouse_y                    
                    selecting_zoom_area = True
                elif (mandlebrot_button.is_over(mouse_x, mouse_y)):
                    mandlebrot_button_clicked()
                elif (zoom_button.is_over(mouse_x, mouse_y)):
                    zoom_button_clicked()
                elif (inc_zoom_button.is_over(mouse_x, mouse_y)):
                    inc_zoom_button_clicked()
                elif (dec_zoom_button.is_over(mouse_x, mouse_y)):
                    dec_zoom_button_clicked()
            elif event.type == pygame.MOUSEBUTTONUP:
                if (selecting_zoom_area):
                    selecting_zoom_area = False

        pygame.display.update()
        clock.tick(CLOCK_TICK)
    pygame.quit()

###############################################
# mandlebrot_button_clicked()
###############################################

def mandlebrot_button_clicked():
    pass

###############################################
# zoom_button_clicked()
###############################################

def zoom_button_clicked():
    pass

###############################################
# inc_zoom_button_clicked()
###############################################

def inc_zoom_button_clicked():
    global zoom_steps
    zoom_steps = min(zoom_steps + 1, MAX_ZOOM_STEPS)
    zoom_button.set_label(ZOOM_BUTTON_LABEL.format(zoom_steps))
    zoom_button.draw(screen)

###############################################
# dec_zoom_button_clicked()
###############################################

def dec_zoom_button_clicked():
    global zoom_steps
    zoom_steps = max(zoom_steps - 1, MIN_ZOOM_STEPS)
    zoom_button.set_label(ZOOM_BUTTON_LABEL.format(zoom_steps))
    zoom_button.draw(screen)

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

