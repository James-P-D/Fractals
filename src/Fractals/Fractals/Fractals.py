import pygame  # Tested with pygame v1.9.6
import numpy as np
import datetime
from Constants import *
from UIControls import *
from MandlebrotFractal import mandlebrot_fractal
from JuliaFractal import julia_fractal
import threading

###############################################
# Globals
###############################################

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

zoom_steps = MIN_ZOOM_STEPS

mandlebrot_button = Button((LARGE_BUTTON_WIDTH * 0),
                           BUTTON_STRIP_TOP,
                           LARGE_BUTTON_WIDTH,
                           LARGE_BUTTON_HEIGHT,
                           MANDLEBROT_BUTTON_LABEL)
julia_button = Button((LARGE_BUTTON_WIDTH * 1),
                      BUTTON_STRIP_TOP,
                      LARGE_BUTTON_WIDTH,
                      LARGE_BUTTON_HEIGHT,
                      JULIA_BUTTON_LABEL)
zoom_button = Button((LARGE_BUTTON_WIDTH * 2),
                     BUTTON_STRIP_TOP,
                     LARGE_BUTTON_WIDTH,
                     LARGE_BUTTON_HEIGHT,
                     ZOOM_BUTTON_LABEL.format(zoom_steps))
inc_zoom_button = Button((SMALL_BUTTON_WIDTH * 0) +
                         (LARGE_BUTTON_WIDTH * TOTAL_LARGE_BUTTONS),
                         BUTTON_STRIP_TOP,
                         SMALL_BUTTON_WIDTH,
                         SMALL_BUTTON_HEIGHT,
                         ZOOM_INC_BUTTON_LABEL)
dec_zoom_button = Button((SMALL_BUTTON_WIDTH * 1) +
                         (LARGE_BUTTON_WIDTH * TOTAL_LARGE_BUTTONS),
                         BUTTON_STRIP_TOP,
                         SMALL_BUTTON_WIDTH,
                         SMALL_BUTTON_HEIGHT,
                         ZOOM_DEC_BUTTON_LABEL)

processing = False
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
            if (event.type == pygame.QUIT) and (not processing):
                game_exit = True
            elif ((event.type == pygame.MOUSEMOTION) and
                  (selecting_zoom_area) and
                  (not processing)):
                # Flip the existing rectangle to remove it
                flip_rect(zoom_x1,
                          zoom_x2,
                          zoom_y1,
                          zoom_y2,
                          1 if zoom_x1 < zoom_x2 else -1,
                          1 if zoom_y1 < zoom_y2 else -1)
                # Get the new (zoom_x2, zoom_y2) corner
                (zoom_x2, zoom_y2) = pygame.mouse.get_pos()
                # Make sure zoom_y2 is no lower than the bottom of the canvas
                zoom_y2 = min(CANVAS_HEIGHT - 1, zoom_y2)
                # Draw the new rectangle with a new (x2, y2) corner
                flip_rect(zoom_x1,
                          zoom_x2,
                          zoom_y1,
                          zoom_y2,
                          1 if zoom_x1 < zoom_x2 else -1,
                          1 if zoom_y1 < zoom_y2 else -1)
                # Finally set the zoom_set flag
                zoom_set = True

            elif (event.type == pygame.MOUSEBUTTONDOWN) and (not processing):
                (mouse_x, mouse_y) = pygame.mouse.get_pos()
                if (mouse_y < CANVAS_HEIGHT):
                    # If zoom_x1, zoom_y1, zoom_x2, zoom_y2 are all nan,
                    # then we have already drawn an rectangle on screen
                    # Draw it again to overwrite it before we draw a new one

                    if (zoom_set):
                        flip_rect(zoom_x1,
                                  zoom_x2,
                                  zoom_y1,
                                  zoom_y2,
                                  1 if zoom_x1 < zoom_x2 else -1,
                                  1 if zoom_y1 < zoom_y2 else -1)

                    zoom_x1 = zoom_x2 = mouse_x
                    zoom_y1 = zoom_y2 = mouse_y
                    selecting_zoom_area = True
                elif (mandlebrot_button.is_over(mouse_x, mouse_y)):
                    thread = threading.Thread(target=mandlebrot_button_clicked,
                                              args=())
                    thread.start()
                elif (julia_button.is_over(mouse_x, mouse_y)):
                    thread = threading.Thread(target=julia_button_clicked,
                                              args=())
                    thread.start()
                elif (zoom_button.is_over(mouse_x, mouse_y)):
                    thread = threading.Thread(target=zoom_button_clicked,
                                              args=())
                    thread.start()
                elif (inc_zoom_button.is_over(mouse_x, mouse_y)):
                    # Call inc_zoom_button_clicked() to
                    # increment our zoom step by 1
                    inc_zoom_button_clicked()
                    # Set a flag to say inc button has been pressed,
                    # incase user holds mouse button down
                    clicking_inc_zoom = True
                    # Don't auto-increment the zoom step unless button
                    # has been held down for 1 full second
                    next_inc_zoom_time = (datetime.datetime.now() +
                                          datetime.timedelta(0, 1))
                elif (dec_zoom_button.is_over(mouse_x, mouse_y)):
                    # Call dec_zoom_button_clicked() to
                    # decrement our zoom step by 1
                    dec_zoom_button_clicked()
                    # Set a flag to say decc button has been
                    # pressed, incase user holds mouse button down
                    clicking_dec_zoom = True
                    # Don't auto-decrement the zoom step unless
                    # button has been held down for 1 full second
                    next_dec_zoom_time = (datetime.datetime.now() +
                                          datetime.timedelta(0, 1))
            elif (event.type == pygame.MOUSEBUTTONUP) and (not processing):
                selecting_zoom_area = False
                clicking_inc_zoom = False
                clicking_dec_zoom = False

        if (clicking_inc_zoom and (datetime.datetime.now() > next_inc_zoom_time) and (not processing)):
            inc_zoom_button_clicked()
            # For any future increments, only wait 500ms
            next_inc_zoom_time = (datetime.datetime.now() +
                                  datetime.timedelta(0, 0, 500))
        elif (clicking_dec_zoom and
              (datetime.datetime.now() > next_dec_zoom_time) and
              (not processing)):
            dec_zoom_button_clicked()
            # For any future decrements, only wait 500ms
            next_dec_zoom_time = (datetime.datetime.now() +
                                  datetime.timedelta(0, 0, 500))

        pygame.display.update()
        clock.tick(CLOCK_TICK)
    pygame.quit()


###############################################
# mandlebrot_button_clicked()
###############################################

def mandlebrot_button_clicked():
    global processing
    processing = True

    global current_fractal
    current_fractal = MANDLEBROT_FRACTAL

    global zoom_x1, zoom_y1, zoom_x2, zoom_y2
    (zoom_x1, zoom_y1, zoom_x2, zoom_y2) = (0, 0, 0, 0)

    global zoom_set
    zoom_set = False

    global min_x, min_y, max_x, max_y
    (min_x, min_y, max_x, max_y) = (MANDLEBROT_MIN_X,
                                    MANDLEBROT_MIN_Y,
                                    MANDLEBROT_MAX_X,
                                    MANDLEBROT_MAX_Y)

    start_time = datetime.datetime.now()
    if (USE_JULIA):
        from julia import Main
        Main.include('library.jl')
        draw_fractal(Main.mandlebrot_fractal(min_x,
                                             min_y,
                                             max_x,
                                             max_y,
                                             CANVAS_WIDTH,
                                             CANVAS_HEIGHT,
                                             MANDLEBROT_ITERATIONS))
        print("Done!")
    else:
        draw_fractal(mandlebrot_fractal(min_x, min_y, max_x, max_y))
    end_time = datetime.datetime.now()
    diff = end_time - start_time
    print("Fractal generated in ", diff.seconds, "s")

    processing = False


###############################################
# julia_button_clicked()
###############################################

def julia_button_clicked():
    global processing
    processing = True

    global current_fractal
    current_fractal = JULIA_FRACTAL

    global zoom_x1, zoom_y1, zoom_x2, zoom_y2
    (zoom_x1, zoom_y1, zoom_x2, zoom_y2) = (0, 0, 0, 0)

    global zoom_set
    zoom_set = False

    global min_x, min_y, max_x, max_y
    (min_x, min_y, max_x, max_y) = (JULIA_MIN_X,
                                    JULIA_MIN_Y,
                                    JULIA_MAX_X,
                                    JULIA_MAX_Y)

    start_time = datetime.datetime.now()
    if (USE_JULIA):
        from julia import Main
        Main.include('library.jl')
        draw_fractal(Main.julia_fractal(min_x,
                                        min_y,
                                        max_x,
                                        max_y,
                                        CANVAS_WIDTH,
                                        CANVAS_HEIGHT,
                                        MANDLEBROT_ITERATIONS))
        print("Done!")
    else:
        draw_fractal(julia_fractal(min_x, min_y, max_x, max_y))
    end_time = datetime.datetime.now()
    diff = end_time - start_time
    print("Fractal generated in ", diff.seconds, "s")

    processing = False


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

    global processing
    processing = True

    global zoom_x1, zoom_y1, zoom_x2, zoom_y2
    if (zoom_x2 < zoom_x1):
        (zoom_x1, zoom_x2) = (zoom_x2, zoom_x1)
    if (zoom_y2 < zoom_y1):
        (zoom_y1, zoom_y2) = (zoom_y2, zoom_y1)

    global min_x, min_y, max_x, max_y
    x_pixel_diff = (max_x - min_x) / CANVAS_WIDTH
    y_pixel_diff = (max_y - min_y) / CANVAS_HEIGHT

    x1_zoom_step = ((zoom_x1 * x_pixel_diff)) / (zoom_steps + 1)
    y1_zoom_step = ((zoom_y1 * y_pixel_diff)) / (zoom_steps + 1)
    x2_zoom_step = ((max_x -
                     ((zoom_x2 * x_pixel_diff) + min_x)) / (zoom_steps + 1))
    y2_zoom_step = ((max_y -
                     ((zoom_y2 * y_pixel_diff) + min_y)) / (zoom_steps + 1))

    for step in range(zoom_steps + 1):
        min_x += x1_zoom_step
        min_y += y1_zoom_step
        max_x -= x2_zoom_step
        max_y -= y2_zoom_step
        print(f"Zoom step {step+1} of {zoom_steps + 1}")
        start_time = datetime.datetime.now()

        if (current_fractal == MANDLEBROT_FRACTAL):
            draw_fractal(mandlebrot_fractal(min_x, min_y, max_x, max_y))
        elif (current_fractal == JULIA_FRACTAL):
            draw_fractal(julia_fractal(min_x, min_y, max_x, max_y))

        end_time = datetime.datetime.now()
        diff = end_time - start_time
        print("Fractal generated in ", diff.seconds, "s")

    zoom_set = False
    processing = False


###############################################
# draw_fractal()
###############################################

def draw_fractal(pixels):
    new_surface = pygame.surfarray.make_surface(pixels)
    screen.blit(new_surface, (0, 0))
    pygame.display.flip()


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
    pygame.display.set_caption("Fractals")
    screen.fill(BLACK)
    mandlebrot_button.draw(screen)
    julia_button.draw(screen)
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
