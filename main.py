from turtle import Screen
import time
from Snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.title("--Snake Game--")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food1 = Food()
food2 = Food()
food3 = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")
screen.onkey(snake.left, "a")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food1) < 15:
        food1.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.distance(food2) < 15:
        food2.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.distance(food3) < 15:
        food3.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
