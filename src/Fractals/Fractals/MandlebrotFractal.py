import numpy as np
from Constants import *
  
def calc(x, y, iterations): 
    c0 = complex(x, y) 
    c = 0
    for i in range(1, iterations): 
        if abs(c) > 2: 
            return i
        c = c * c + c0 
    return 0

def mandlebrot_fractal(min_x, min_y, max_x, max_y):
    pixels = np.ndarray((CANVAS_WIDTH, CANVAS_HEIGHT), int)
    x_pixel_diff = (max_x - min_x) / CANVAS_WIDTH
    y_pixel_diff = (max_y - min_y) / CANVAS_HEIGHT

    for x in range(CANVAS_WIDTH):  
        for y in range(CANVAS_HEIGHT): 
            i = calc((x * x_pixel_diff) + min_x, (y * y_pixel_diff) + min_y, MANDLEBROT_ITERATIONS)            
            pixels[x,y] = (i << 21) + (i << 10) + i * 8
    return pixels    
