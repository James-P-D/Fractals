# Fractals
Fractals with zoom functionality in Python and Julia

![Screenshot](https://github.com/James-P-D/Fractals/blob/master/screenshot.gif)

## Usage



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