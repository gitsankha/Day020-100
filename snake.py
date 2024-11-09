import turtle

class Snake:
    def __init__(self):
        self.shape = "square"
        self.color = "white"
        self.segment = []
        self.turtle_pos = [(0,0), (-20,0), (-40,0)]
        self.nx = 0
        self.ny = 0
        for i in range(3):
            self.new_turtle = turtle.Turtle(self.shape)
            self.new_turtle.color(self.color)
            self.new_turtle.pu()
            self.new_turtle.goto(self.turtle_pos[i])
            self.segment.append(self.new_turtle)
        self.head = self.segment[0]

    def move(self):
        for i in range(2,0,-1):
            self.nx = self.segment[i-1].xcor()
            self.ny = self.segment[i-1].ycor()
            self.segment[i].goto(self.nx, self.ny)
        self.head.fd(20)
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
