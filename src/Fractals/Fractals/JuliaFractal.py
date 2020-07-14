import datetime
import pygame
import numpy as np
from Constants import *

def draw_julia_fractal(min_x, min_y, max_x, max_y, screen):
    cX, cY = -0.7, 0.27015
    maxIter = JULIA_ITERATIONS
   
    x_pixel_diff = (max_x - min_x) / CANVAS_WIDTH
    y_pixel_diff = (max_y - min_y) / CANVAS_HEIGHT

    for x in range(CANVAS_WIDTH): 
        for y in range(CANVAS_HEIGHT): 
            zx = (x * x_pixel_diff) + min_x
            zy = (y * y_pixel_diff) + min_y
            i = maxIter 
            while zx*zx + zy*zy < 4 and i > 1: 
                tmp = zx*zx - zy*zy + cX 
                zy,zx = 2.0*zx*zy + cY, tmp 
                i -= 1
  
            screen.set_at((x, y), (i << 21) + (i << 10) + i*8)