import os

#Windon Scale for Pygames
WIDTH = 800
HEIGHT = 600

#GAME SPEED
FPS = 120


#TITLE and Icon

TITLE = "Solitarie Python Project"
ICON = "C:\oop\Python_AI\Python_project\solitaire_python_pygames\image\icon.png"

#Colors

WHITE = (255,255,255)
BLACK = (0 ,0 ,0)
RED = (255, 0, 0)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)


#Image Card PathWay

project_folder = os.path.dirname(__file__)
image_folder = os.path.join(project_folder, "image")
card_folder = os.path.join(image_folder, "cards")

