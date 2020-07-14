import datetime
import colorsys
import pygame
import numpy as np
from Constants import *

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

def draw_mandlebrot(min_x, min_y, max_x, max_y, screen):
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
