import pygame # Tested with pygame v1.9.6
import numpy as np
#from numpy import complex, array 
from Constants import *
from UIControls import *
import datetime
import colorsys

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

zoom_steps = MIN_ZOOM_STEPS

mandlebrot_button = Button((LARGE_BUTTON_WIDTH * 0), BUTTON_STRIP_TOP, LARGE_BUTTON_WIDTH, LARGE_BUTTON_HEIGHT, MANDLEBROT_BUTTON_LABEL)
zoom_button = Button((LARGE_BUTTON_WIDTH * 1), BUTTON_STRIP_TOP, LARGE_BUTTON_WIDTH, LARGE_BUTTON_HEIGHT, ZOOM_BUTTON_LABEL.format(zoom_steps))
inc_zoom_button = Button((SMALL_BUTTON_WIDTH * 0) + (LARGE_BUTTON_WIDTH * TOTAL_LARGE_BUTTONS), BUTTON_STRIP_TOP, SMALL_BUTTON_WIDTH, SMALL_BUTTON_HEIGHT, ZOOM_INC_BUTTON_LABEL)
dec_zoom_button = Button((SMALL_BUTTON_WIDTH * 1) + (LARGE_BUTTON_WIDTH * TOTAL_LARGE_BUTTONS), BUTTON_STRIP_TOP, SMALL_BUTTON_WIDTH, SMALL_BUTTON_HEIGHT, ZOOM_DEC_BUTTON_LABEL)

zoom_set = False
(min_x, min_y, max_x, max_y) = (0, 0, 0, 0)
(zoom_x1, zoom_y1, zoom_x2, zoom_y2) = (0, 0, 0, 0)

current_fractal = NO_FRACTAL

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
    global zoom_x1, zoom_y1, zoom_x2, zoom_y2    
    global zoom_set

    clicking_inc_zoom = clicking_dec_zoom = False
    next_inc_zoom_time = next_dec_zoom_time = None

    while not game_exit:
        pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True;
            elif (event.type == pygame.MOUSEMOTION) and (selecting_zoom_area) :    
                # Flip the existing rectangle to remove it
                flip_rect(zoom_x1, zoom_x2, zoom_y1, zoom_y2, 1 if zoom_x1 < zoom_x2 else -1, 1 if zoom_y1 < zoom_y2 else -1)                
                # Get the new (zoom_x2, zoom_y2) corner
                (zoom_x2, zoom_y2) = pygame.mouse.get_pos()
                # Make sure zoom_y2 is no lower than the bottom of the canvas
                zoom_y2 = min(CANVAS_HEIGHT - 1, zoom_y2)
                # Draw the new rectangle with a new (x2, y2) corner
                flip_rect(zoom_x1, zoom_x2, zoom_y1, zoom_y2, 1 if zoom_x1 < zoom_x2 else -1, 1 if zoom_y1 < zoom_y2 else -1)
                # Finally set the zoom_set flag
                zoom_set = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                (mouse_x, mouse_y) = pygame.mouse.get_pos()
                if (mouse_y < CANVAS_HEIGHT):
                    # If zoom_x1, zoom_y1, zoom_x2, zoom_y2 are all nan, then we have already drawn an rectangle on screen
                    # Draw it again to overwrite it before we draw a new one
                    
                    if (zoom_set):
                        flip_rect(zoom_x1, zoom_x2, zoom_y1, zoom_y2, 1 if zoom_x1 < zoom_x2 else -1, 1 if zoom_y1 < zoom_y2 else -1)
                
                    zoom_x1 = zoom_x2 = mouse_x
                    zoom_y1 = zoom_y2 = mouse_y                    
                    selecting_zoom_area = True                    
                elif (mandlebrot_button.is_over(mouse_x, mouse_y)):
                    mandlebrot_button_clicked()
                elif (zoom_button.is_over(mouse_x, mouse_y)):
                    zoom_button_clicked()
                elif (inc_zoom_button.is_over(mouse_x, mouse_y)):
                    # Call inc_zoom_button_clicked() to increment our zoom step by 1
                    inc_zoom_button_clicked()
                    # Set a flag to say inc button has been pressed, incase user holds mouse button down
                    clicking_inc_zoom = True
                    # Don't auto-increment the zoom step unless button has been held down for 1 full second
                    next_inc_zoom_time = datetime.datetime.now() + datetime.timedelta(0, 1)
                elif (dec_zoom_button.is_over(mouse_x, mouse_y)):
                    # Call dec_zoom_button_clicked() to decrement our zoom step by 1
                    dec_zoom_button_clicked()
                    # Set a flag to say decc button has been pressed, incase user holds mouse button down
                    clicking_dec_zoom = True
                    # Don't auto-decrement the zoom step unless button has been held down for 1 full second
                    next_dec_zoom_time = datetime.datetime.now() + datetime.timedelta(0, 1)
            elif event.type == pygame.MOUSEBUTTONUP:
                selecting_zoom_area = False
                clicking_inc_zoom = False
                clicking_dec_zoom = False
            
        if clicking_inc_zoom and (datetime.datetime.now() > next_inc_zoom_time):
            inc_zoom_button_clicked()
            # For any future increments, only wait 500ms
            next_inc_zoom_time = datetime.datetime.now() + datetime.timedelta(0, 0, 500)
        elif clicking_dec_zoom and (datetime.datetime.now() > next_dec_zoom_time):
            dec_zoom_button_clicked()
            # For any future decrements, only wait 500ms
            next_dec_zoom_time = datetime.datetime.now() + datetime.timedelta(0, 0, 500)

        pygame.display.update()
        clock.tick(CLOCK_TICK)
    pygame.quit()

###############################################
# mandlebrot_button_clicked()
###############################################
def rgb_conv(i): 
    color = 255 * np.array(colorsys.hsv_to_rgb(i / 255.0, 1.0, 0.5)) 
    return tuple(color.astype(int)) 
  
def mandelbrot(x, y, iterations): 
    c0 = complex(x, y) 
    c = 0
    for i in range(1, iterations): 
        if abs(c) > 2: 
            return rgb_conv(i) 
        c = c * c + c0 
    return (0, 0, 0) 

def draw_mandlebrot():
    x_pixel_diff = (max_x - min_x) / CANVAS_WIDTH
    y_pixel_diff = (max_y - min_y) / CANVAS_HEIGHT

    start_time = datetime.datetime.now()
    for x in range(CANVAS_WIDTH):  
        # displaying the progress as percentage 
        #print("%.2f %%" % (x / CANVAS_WIDTH * 100.0))  
        for y in range(CANVAS_HEIGHT): 
            (r, g, b) = mandelbrot((x * x_pixel_diff) + min_x, (y * y_pixel_diff) + min_y, MANDLEBROT_ITERATIONS)
            screen.set_at((x, y), (r, g, b, 255))
    end_time = datetime.datetime.now()
    diff = end_time - start_time
    print(diff.seconds, "s")

def mandlebrot_button_clicked():    
    global current_fractal
    current_fractal = MANDLEBROT

    global zoom_x1, zoom_y1, zoom_x2, zoom_y2
    (zoom_x1, zoom_y1, zoom_x2, zoom_y2) = (0, 0, 0, 0)
    
    global zoom_set
    zoom_set = False

    global min_x, min_y, max_x, max_y
    (min_x, min_y, max_x, max_y) = (MANDLEBROT_MIN_X, MANDLEBROT_MIN_Y, MANDLEBROT_MAX_X, MANDLEBROT_MAX_Y)
    
    draw_mandlebrot()
   
###############################################
# zoom_button_clicked()
###############################################

def zoom_button_clicked():
    global current_fractal
    if (current_fractal == NO_FRACTAL):
        print("You need to draw a fractal first")
        return

    global zoom_set
    if (not zoom_set):
        print("You need to draw a square first")
        return

    global zoom_x1, zoom_y1, zoom_x2, zoom_y2
    if (zoom_x2 < zoom_x1):
        (zoom_x1, zoom_x2) = (zoom_x2, zoom_x1)
    if (zoom_y2 < zoom_y1):
        (zoom_y1, zoom_y2) = (zoom_y2, zoom_y1)

    global min_x, min_y, max_x, max_y    
    x_pixel_diff = (max_x - min_x) / CANVAS_WIDTH
    y_pixel_diff = (max_y - min_y) / CANVAS_HEIGHT

    print((min_x, min_y, max_x, max_y))

    original_min_x = min_x
    original_min_y = min_y
    min_x = (zoom_x1 * x_pixel_diff) + original_min_x
    min_y = (zoom_y1 * y_pixel_diff) + original_min_y
    max_x = (zoom_x2 * x_pixel_diff) + original_min_x
    max_y = (zoom_y2 * y_pixel_diff) + original_min_y

    print((min_x, min_y, max_x, max_y))

    draw_mandlebrot()

    zoom_set = False

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

