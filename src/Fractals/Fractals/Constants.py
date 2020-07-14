CANVAS_WIDTH = 500
CANVAS_HEIGHT = 300

BUTTON_HEIGHT = 50

WINDOW_WIDTH = CANVAS_WIDTH
WINDOW_HEIGHT = CANVAS_HEIGHT + BUTTON_HEIGHT

###############################################
# RGB Colors
###############################################

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_GRAY = (211, 211, 211)
DARK_GRAY = (140, 140, 140)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

###############################################
# Button sizes
###############################################

BUTTON_STRIP_TOP = CANVAS_HEIGHT

TOTAL_SMALL_BUTTONS = 2
TOTAL_LARGE_BUTTONS = 3

SMALL_BUTTON_HEIGHT = BUTTON_HEIGHT
SMALL_BUTTON_WIDTH = SMALL_BUTTON_HEIGHT

LARGE_BUTTON_HEIGHT = BUTTON_HEIGHT
LARGE_BUTTON_WIDTH = (WINDOW_WIDTH - (SMALL_BUTTON_WIDTH * TOTAL_SMALL_BUTTONS)) / TOTAL_LARGE_BUTTONS

MANDLEBROT_BUTTON_LABEL = "Mandlebrot"
JULIA_BUTTON_LABEL = "Julia"

ZOOM_BUTTON_LABEL = "Zoom Steps: {0}"
ZOOM_INC_BUTTON_LABEL = "+"
ZOOM_DEC_BUTTON_LABEL = "-"

BUTTON_BORDER_COLOR = WHITE
BUTTON_COLOR = BLACK
BUTTON_LABEL_COLOR = WHITE

BUTTON_BORDER_SIZE = 2

BUTTON_FONT_SIZE = 15

###############################################
# Zooming
###############################################

MIN_ZOOM_STEPS = 1
MAX_ZOOM_STEPS = 100

###############################################
# Fractal Types
###############################################

NO_FRACTAL = 0
MANDLEBROT_FRACTAL = 1
JULIA_FRACTAL = 2

###############################################
# Mandlebrot Fractal
###############################################

MANDLEBROT_MIN_X = -3.0
MANDLEBROT_MIN_Y = -1.0
MANDLEBROT_MAX_X = 1.0
MANDLEBROT_MAX_Y = 1.0

MANDLEBROT_ITERATIONS = 100

###############################################
# Julia Fractal
###############################################

JULIA_MIN_X = -1.5
JULIA_MIN_Y = -1.0
JULIA_MAX_X = 1.5
JULIA_MAX_Y = 1.0

JULIA_ITERATIONS = 100

###############################################
# PyGame
###############################################

CLOCK_TICK = 30
