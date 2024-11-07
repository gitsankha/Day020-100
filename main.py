import turtle

screen = turtle.Screen()
screen.setup(height=600,width=600)
screen.title("My Sanke Xanzia")
screen.bgcolor("black")

# color = ['white', 'red', 'green']
all_turtles = []
turtle_pos = [(0,0),(-20,0),(-40,0)]

for i in range(0,3):
    new_turtle = turtle.Turtle()
    new_turtle.shape("square")
    new_turtle.color("white")
    new_turtle.setpos(turtle_pos[i])











screen.exitonclick()
