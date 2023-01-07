from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
# total=[]

# for n in range(3):
#     block=Turtle(shape="square")
#     block.penup()
#     block.color("white")
#     block.setx(0-n*20)
#     total.append(block)

screen.update()

game_is_on=True

while game_is_on:
    screen.update()
    snake.move()
#detect collision with food
    if snake.head.distance(food)<20:
        food.refresh()
        scoreboard.update_score()
        snake.extend()

    #detect collision
    if snake.head.xcor()>295 or snake.head.xcor()<-295 or snake.head.ycor()>295 or snake.head.ycor()<-295:
        scoreboard.reset()
        snake.reset()

    #Detect collision with tail
    for segment in snake.total[1:]:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment)<10:
            scoreboard.reset()
            snake.reset()
    #if haed collides with any segment in the tail:
        #trigger game_over


    # for number in range(len(total)-1,0,-1):
    #     x=total[number-1].xcor()
    #     y=total[number-1].ycor()
    #     total[number].goto(x,y)
    # total[0].forward(20)
    #total[0].left(90)
    time.sleep(0.09)











screen.exitonclick()