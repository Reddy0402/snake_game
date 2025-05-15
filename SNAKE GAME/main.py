from turtle import Screen,Turtle
import time
from food import Food
from scoreboard import Scoreboard
from snake import Snake

new_segment = Turtle()
screen = Screen()
screen.setup(width=600,height=600)
screen.title("anaconda")
screen.bgcolor("black")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()



screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right, "Right")

game_active = True
while game_active:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #food detection
    if snake.head.distance(food)<15:
        food.refresh1()
        snake.extend()
        scoreboard.inc_score()


    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        scoreboard.reset()
        snake.reset()





    for segments in snake.segments[1:3]:
        # print(snake.head.distance(segments) < 10)
        if snake.head.distance(segments) < 10:
            scoreboard.reset()
            snake.reset()


















screen.exitonclick()