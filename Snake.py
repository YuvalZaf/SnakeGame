from turtle import Turtle
START_POS = [(0, 0), (-20, 0), (-40, 0)]  # build the first snake
MOVE_LENGTH = 20


class Snake(Turtle):
    def __init__(self):  # constructor
        super().__init__()
        self.segments = []
        self.make_snake()
        self.snake_head = self.segments[0]

    def make_snake(self):  # create the snake
        for i in START_POS:
            snake = Turtle()
            snake.penup()
            snake.shape("square")
            snake.color("white")
            snake.goto(i)
            self.segments.append(snake)

    def move(self):  # move the snake always forward
        for i in range(len(self.segments) - 1, 0, -1):  # copy the segment before you
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].goto(x, y)
        self.snake_head.forward(MOVE_LENGTH)

    def go_up(self):
        if self.snake_head.heading() != 270:
            self.snake_head.setheading(90)

    def go_down(self):
        if self.snake_head.heading() != 90:
            self.snake_head.setheading(270)

    def go_right(self):
        if self.snake_head.heading() != 180:
            self.snake_head.setheading(0)

    def go_left(self):
        if self.snake_head.heading() != 0:
            self.snake_head.setheading(180)

    def add_seg(self):  # snake become larger
        new_seg = Turtle()
        new_seg.penup()
        new_seg.shape("square")
        new_seg.color("white")
        self.segments.append(new_seg)
