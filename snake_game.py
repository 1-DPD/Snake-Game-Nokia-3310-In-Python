from turtle import Turtle
SNAKE_POSITION = [(0, 0), (20, 0), (40, 0)]
DISTANCE_MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_body_segment = []
        self.create_snake()
        self.snake_head = self.snake_body_segment[0]

    def create_snake(self):
        for position in SNAKE_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        snake_body = Turtle("square")
        snake_body.color("white")
        snake_body.penup()
        snake_body.goto(position)
        self.snake_body_segment.append(snake_body)

    def extend_snake_body(self):
        self.add_segment(self.snake_body_segment[-1].position())

    def snake_movement(self):
        for segment in range(len(self.snake_body_segment) - 1, 0, -1):
            x_position = self.snake_body_segment[segment - 1].xcor()
            y_position = self.snake_body_segment[segment - 1].ycor()
            self.snake_body_segment[segment].goto(x_position, y_position)
        self.snake_head.forward(DISTANCE_MOVE)

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)
