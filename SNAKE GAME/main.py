from tkinter import *
import random

#constants defined
GAME_WIDTH = 800
GAME_HEIGHT = 800
SPEED = 50
SPACE_SIZE = 50
BACKGROUND_COLOR = "#000000"
FOOD_COLOR = "#FF0000"
SNAKE_COLOR = "#00FF00"


class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coodinates =[]
        self.squares= []

        for i in range (0, BODY_PARTS):
            self.coordinates.append([0, 0])
    pass

class Food:

    def __init__(self):
        x= random.randint(0,(GAME_WIDTH/SPACE_SIZE)-1 )*SPACE_SIZE
        y= random.randint(0,(GAME_HEIGHT/SPACE_SIZE)-1 )*SPACE_SIZE

        self.coordinates = [x, y]
        canvas.create_oval (x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill = FOOD_COLOR, tag = Food) 

    pass

def next_turn():
    pass

def change_direction(new_direction):
    pass

def check_collisions():
    pass

def game_over():
    pass


window = Tk()
window.title("Snake Game")
window.resizable(True, True)
score = 0
direction = "up"
label = Label(window, text = "Score:{}".format(score), font = ("Annabelle", 40 ))
label.pack()
canvas = Canvas(window, background = BACKGROUND_COLOR, width =GAME_WIDTH, height = GAME_HEIGHT)
canvas.pack()

window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

#adjusting window position
x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))


window.geometry(f"{window_height}x{window_width}+{y}+{x}")

snake = Snake()
food = Food()




window.mainloop ()

