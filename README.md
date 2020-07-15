# Fractals
Fractals with zoom functionality in Python and Julia

![Screenshot](https://github.com/James-P-D/Fractals/blob/master/screenshot.gif)

## Usage

After running the application you will be presented with a blank canvas and a series of buttons. Press <kbd>Mandlebrot</kbd> button to generate the [Mandlebrot Set](https://en.wikipedia.org/wiki/Mandelbrot_set) or hit <kbd>Julia</kbd> to generate the [Julia Set](https://en.wikipedia.org/wiki/Julia_set).

Once generated you can select a section you wish to zoom to by creating a rectangle using your mouse. Once selected press the <kbd>Zoom</kbd> button to zoom to the selected section.

By default the application will zoom straight to the selected section. If you would like to increase or decrease the number of intermediate steps during the zoom process, simply use the <kbd>+</kbd> and <kbd>-</kbd> buttons respectively.

## Python/Julia

When I first created the application, both fractals were calculated in Python (see [MandlebrotFractal.py](https://github.com/James-P-D/Fractals/blob/master/src/Fractals/Fractals/MandlebrotFractal.py) and [JuliaFractal.py](https://github.com/James-P-D/Fractals/blob/master/src/Fractals/Fractals/JuliaFractal.py)) but was disappointed with the time taken to generate them. Since I'd heard [Julia](https://julialang.org/) is fast I decided to reimplement both fractals. Whilst the code works (see [Library.jl](https://github.com/James-P-D/Fractals/blob/master/src/Fractals/Fractals/Library.jl)), it doesn't appear to like being called on a thread, so this has been temporarily disabled.

If you want to try using the Julia-generated fractals, set `USE_JULIA` to `False` in [Constants.py](https://github.com/James-P-D/Fractals/blob/master/src/Fractals/Fractals/Constants.py).

## Setup

For Python we need the following:

[pygame](https://www.pygame.org/news) (Tested with v1.9.6)  
[numpy](https://numpy.org/) (Tested with v1.18.3)  
[pyjulia](https://github.com/JuliaPy/pyjulia) (Tested with v0.5.3)  

```
pip install pygame
pip install numpy
pip install julia
```

For Julia we need to install [pycall](https://github.com/JuliaPy/PyCall.jl):

```
julia> using Pkg
julia> Pkg.add("PyCall")
```

I also had to run the following from the Python REPL:

```
>>> import julia
>>> julia.install()
```