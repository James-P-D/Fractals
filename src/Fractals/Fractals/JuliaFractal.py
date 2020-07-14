import datetime
import pygame
import numpy as np
from Constants import *

def draw_julia_fractal(min_x, min_y, max_x, max_y, screen):
    cX, cY = -0.7, 0.27015
    maxIter = JULIA_ITERATIONS
   
    x_pixel_diff = (max_x - min_x) / CANVAS_WIDTH
    y_pixel_diff = (max_y - min_y) / CANVAS_HEIGHT

    start_time = datetime.datetime.now()
    for x in range(CANVAS_WIDTH): 
        for y in range(CANVAS_HEIGHT): 
            zx = (x * x_pixel_diff) + min_x
            zy = (y * y_pixel_diff) + min_y
            i = maxIter 
            while ((((zx * zx) + (zy * zy)) < 4) and (i > 1)): 
                temp = (zx * zx) - (zy * zy) + cX 
                zy = (2.0 * zx * zy) + cY
                zx = temp 
                i -= 1
  
            screen.set_at((x, y), (i << 21) + (i << 10) + i * 8)
    end_time = datetime.datetime.now()
    diff = end_time - start_time
    print(diff.seconds, "s")
