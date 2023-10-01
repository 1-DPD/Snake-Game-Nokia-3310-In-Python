from turtle import Screen
from snake_game import Snake
from snake_food import Food
from snake_score import Score
import time

screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor("black")
screen.title("Snake 3310: The Next Generation")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

continue_game = True

while continue_game:
    screen.update()
    time.sleep(0.1)
    snake.snake_movement()

    if snake.snake_head.distance(food) < 15:
        food.refresh_food_location()
        snake.extend_snake_body()
        score.increasing_score()

    if (snake.snake_head.xcor() > 240 or snake.snake_head.xcor() < -240 or snake.snake_head.ycor() > 240 or
            snake.snake_head.ycor() < -240):
        continue_game = False
        score.game_over()

    for seg in snake.snake_body_segment[1:]:
        if snake.snake_head.distance(seg) < 0:
            continue_game = False
            score.game_over()


screen.exitonclick()
