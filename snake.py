from turtle import Turtle
START =[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.all_obj =[]
        self.create()
        self.head = self.all_obj[0]


    def create(self):
        for position in START:
            self.add_segment(position)


    def move(self):
        for obj in range(len(self.all_obj) - 1, 0, -1):
            new_x = self.all_obj[obj - 1].xcor()
            new_y = self.all_obj[obj - 1].ycor()
            self.all_obj[obj].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def add_segment(self, position):
        new_obj = Turtle("square")
        new_obj.color("white")
        new_obj.penup()
        new_obj.goto(position)
        self.all_obj.append(new_obj)

    def extend(self):
        self.add_segment(self.all_obj[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
         self.head.setheading(RIGHT)



