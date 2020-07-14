import datetime
import pygame
import numpy as np
from Constants import *
  
def calc_julia(x, y, iterations): 
    pass

def calc_x(x):
    return 1.5*(x - CANVAS_WIDTH/2)/(0.5*CANVAS_WIDTH) 

def calc_y(y):
    return 1.0*(y - CANVAS_HEIGHT/2)/(0.5*CANVAS_HEIGHT)

def draw_julia_fractal(min_x, min_y, max_x, max_y, screen):
    cX, cY = -0.7, 0.27015
    maxIter = 255
   
    print(f"x = 0 -> {calc_x(0)}")
    print(f"x = {CANVAS_WIDTH} -> {calc_x(CANVAS_WIDTH)}")
    print(f"y = 0 -> {calc_y(0)}")
    print(f"y = {CANVAS_HEIGHT} -> {calc_y(CANVAS_HEIGHT)}")

    for x in range(CANVAS_WIDTH): 
        for y in range(CANVAS_HEIGHT): 
            zx = calc_x(x)
            zy = calc_y(y)
            i = maxIter 
            while zx*zx + zy*zy < 4 and i > 1: 
                tmp = zx*zx - zy*zy + cX 
                zy,zx = 2.0*zx*zy + cY, tmp 
                i -= 1
  
            screen.set_at((x, y), (i << 21) + (i << 10) + i*8)