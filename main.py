import turtle
from snake import Snake
import time



screen = turtle.Screen()
screen.setup(height=600,width=600)
screen.title("My Snake Xenzia")
screen.bgcolor("black")
screen.tracer(0,0)

is_game_on = True

snake = Snake()
screen.listen()

"""START HERE """
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()









screen.exitonclick()
