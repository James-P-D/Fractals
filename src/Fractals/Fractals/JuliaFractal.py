import numpy as np
from Constants import *


def julia_fractal(min_x, min_y, max_x, max_y):
    pixels = np.ndarray((CANVAS_WIDTH, CANVAS_HEIGHT), int)
    x_pixel_diff = (max_x - min_x) / CANVAS_WIDTH
    y_pixel_diff = (max_y - min_y) / CANVAS_HEIGHT

    cX, cY = -0.7, 0.27015

    for x in range(CANVAS_WIDTH):
        for y in range(CANVAS_HEIGHT):
            zx = (x * x_pixel_diff) + min_x
            zy = (y * y_pixel_diff) + min_y
            i = JULIA_ITERATIONS
            while ((((zx * zx) + (zy * zy)) < 4) and (i > 1)):
                temp = (zx * zx) - (zy * zy) + cX
                zy = (2.0 * zx * zy) + cY
                zx = temp
                i -= 1

            pixels[x, y] = (i << 21) + (i << 10) + i * 8

    return pixels
