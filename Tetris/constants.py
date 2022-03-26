from game.casting.color import Color

# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GAME
GAME_NAME = "Tetris"
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 680
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE_PATH = "cse210-06/Tetris/assets/fonts"
FONT_FILE = FONT_FILE_PATH + "\\zorque.otf"
FONT_SMALL = 32
FONT_LARGE = 48

# SOUND
SOUNDS_PATH = "cse210-06/Tetris/assets/sounds"
BOUNCE_SOUND = SOUNDS_PATH + "\\boing.wav"
WELCOME_SOUND = SOUNDS_PATH + "\\start.wav"
OVER_SOUND = SOUNDS_PATH + "\\over.wav"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)

# KEYS
LEFT = "left"
RIGHT = "right"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"

# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
GAME_OVER = 4

# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# STATS
STATS_GROUP = "stats"

# HUD
HUD_MARGIN = 15
LEVEL_GROUP = "level"
SCORE_GROUP = "score"
LEVEL_FORMAT = "LEVEL: {}"
SCORE_FORMAT = "SCORE: {}"

# BRICK
BRICK_GROUP = "bricks"
IMAGES_PATH = "cse210-06/Tetris/assets/images"
BRICK_IMAGES = {
    "b": [IMAGES_PATH + f"\\{i:03}.png" for i in range(10,19)],
    "g": [IMAGES_PATH + f"\\{i:03}.png" for i in range(20,29)],
    "p": [IMAGES_PATH + f"\\{i:03}.png" for i in range(30,39)],
    "y": [IMAGES_PATH + f"\\{i:03}.png" for i in range(40,49)]
}
BRICK_WIDTH = 80
BRICK_HEIGHT = 28
BRICK_DELAY = 0.5
BRICK_RATE = 4
BRICK_POINTS = 50

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
PREP_TO_LAUNCH = "PREPARING TO LAUNCH"
WAS_GOOD_GAME = "GAME OVER"