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
    pass

class Food:
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
window.width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

#adjusting window position
x = (screen_width*0.5) - (window_width*0.5)
y = (screen_height*0.5) - (window_height*0.5)

window.geometry(f"{window_height}*{window_width}")

window.mainloop ()

