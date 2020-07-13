CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 500
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
TOTAL_LARGE_BUTTONS = 2

SMALL_BUTTON_HEIGHT = BUTTON_HEIGHT
SMALL_BUTTON_WIDTH = SMALL_BUTTON_HEIGHT

LARGE_BUTTON_HEIGHT = BUTTON_HEIGHT
LARGE_BUTTON_WIDTH = (WINDOW_WIDTH - (SMALL_BUTTON_WIDTH * TOTAL_SMALL_BUTTONS)) / TOTAL_LARGE_BUTTONS

MANDLEBROT_BUTTON_LABEL = "Mandlebrot"
ZOOM_BUTTON_LABEL = "Zoom Steps: {0}"
ZOOM_INC_BUTTON_LABEL = "+"
ZOOM_DEC_BUTTON_LABEL = "-"

BUTTON_BORDER_COLOR = WHITE
BUTTON_COLOR = BLACK
BUTTON_LABEL_COLOR = WHITE

BUTTON_BORDER_SIZE = 2

BUTTON_FONT_SIZE = 20

###############################################
# Zooming
###############################################

MIN_ZOOM_STEPS = 1
MAX_ZOOM_STEPS = 100

###############################################
# PyGame
###############################################

CLOCK_TICK = 30
