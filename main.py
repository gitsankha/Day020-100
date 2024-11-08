import turtle
import time



screen = turtle.Screen()
screen.setup(height=600,width=600)
screen.title("My Snake Xenzia")
screen.bgcolor("black")
# screen.delay(100)
screen.tracer(0,0)
# color = ['white', 'red', 'green']
all_turtles = []
turtle_pos = [(0,0),(-20,0),(-40,0)]
segments = []

for i in range(0,3):
    new_turtle = turtle.Turtle("square")
    new_turtle.color("white")
    new_turtle.pu()
    new_turtle.goto(turtle_pos[i])
    segments.append(new_turtle)



is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(1)
    for i in range(len(segments)):
        if i == 0:
            segment_position = tuple(segments[i].position())
            segments[i].left(90)
            segments[i].fd(20)
        else:
            segments[i].goto(segment_position)
            segment_position = tuple(segments[i].position())










screen.exitonclick()
