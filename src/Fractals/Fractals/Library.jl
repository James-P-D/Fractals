function calc(x, y, iterations)
    c0 = complex(x, y) 
    c = 0
    for i = 1:iterations
        if abs(c) > 2
            return i
        end
        c = c * c + c0
    end
    return 0
end

function mandlebrot_fractal(min_x, min_y, max_x, max_y, canvas_width, canvas_height, iterations)
    z = calc(1,2,3)
    pixels = fill(0, canvas_width, canvas_height)

    x_pixel_diff = (max_x - min_x) / canvas_width
    y_pixel_diff = (max_y - min_y) / canvas_height

    for x = 1:canvas_width
        for y = 1:canvas_height
            i = calc((x * x_pixel_diff) + min_x, (y * y_pixel_diff) + min_y, iterations)            
            pixels[x,y] = (i << 21) + (i << 10) + i * 8
        end
    end

    return pixels
end
