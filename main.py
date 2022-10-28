from turtle import Screen as Class_screen
from snake import Snake, SCREEN_HEIGHT, SCREEN_WIDTH, COLORS
from food import Food
from scoreboard import Scoreboard, get_best
import time
import tkinter
from tkinter import messagebox
import random


# Initialize screen
screen = Class_screen()
screen.tracer(0)
screen.setup(height=SCREEN_HEIGHT, width=SCREEN_WIDTH)
screen.bgcolor("black")
screen.title("Classic Snake Game")

# Initialize game
snake = Snake()
food = Food()
score_board = Scoreboard()
game_is_on = True

messagebox.showinfo("Welcome", "Use the 'Left' and 'Right' keys to control the snake.")

# Event listener
screen.listen()
screen.onkey(fun=snake.go_right, key="Right")
screen.onkey(fun=snake.go_left, key="Left")

# Main loop
while game_is_on:
    time.sleep(0.15)
    screen.update()
    snake.move()
    
    # Detect collision with food
    if snake.head.distance(food) <= 17:
        food.refresh()
        score_board.score_up()
        # Add segment to the snake
        location_x = snake.segments[-1].xcor()
        location_y = snake.segments[-1].ycor()
        snake.add_segment(x=location_x, y=location_y)

    # Detect collision with wall
    if -SCREEN_WIDTH * 0.49 > snake.head.xcor() or snake.head.xcor() > SCREEN_WIDTH * 0.49 or \
            -SCREEN_HEIGHT * 0.49 > snake.head.ycor() or snake.head.ycor() > SCREEN_HEIGHT * 0.49:
        # Game over?
        if score_board.game_over():
            game_is_on = False
            break
        else:
            snake.initialize()
            continue

    # Detect collision with the tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # Game over? 
            if score_board.game_over():
                game_is_on = False
                break
            else:
                snake.initialize()
    
screen.exitonclick()
time.sleep(0.2)

# Show scoreboard
# DATABASE
data = get_best()

# Set screen
root = tkinter.Tk()
root.title("SCOREBOARD")
root.config(background="black")
root.minsize(width=int(SCREEN_WIDTH), height=int(SCREEN_HEIGHT))
root.maxsize(width=int(SCREEN_WIDTH), height=int(SCREEN_HEIGHT))

# Set canvas
canvas = tkinter.Canvas(root, width=int(SCREEN_WIDTH), height=int(SCREEN_HEIGHT), background="black") 

# Base positions
y_position = SCREEN_HEIGHT * 0.15
increment = y_position

# Title
canvas.create_text(SCREEN_WIDTH * 0.5, y_position, fill="cyan", text="TOP PLAYERS", font=("Courier", 60))

# Plot in canvas
def plot(x_variation: float, text_: str):
    x_ = SCREEN_WIDTH * x_variation
    y_ = y_position + increment
    canvas.create_text(x_, y_, fill="cyan", text=f"{text_.upper()}", font=("Courier", 40))
    if data is not None:
        for minidict in data:
            y_ += increment
            canvas.create_text(x_, y_, fill=f"{random.choice(COLORS)}", text=f"{minidict[text_]}", font=("Courier", 30))

# Players
plot(0.20, 'player')
# Scores
plot(0.50, 'score')
# Dates
plot(0.80, 'date')
    
canvas.pack(side="top")
root.mainloop()
