from turtle import Turtle,Screen
from paddles import Paddle
from ball import Ball
import time
from score import Score

screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Octucode: Ping Pong")
screen.tracer(0)


r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))

ball=Ball()
score=Score()

screen.listen()

screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")


screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

default_sleep=0.1
while True:

    screen.update()
    time.sleep(default_sleep)
    
    ball.goto(ball.xcor()+ball.x_move, ball.ycor()+ball.y_move)

    #detecting collisiton for the upper and lower edges
    if ball.ycor()>=280 or  ball.ycor()<=-280:
        ball.y_move *=-1

    #detecting collision with the paddles
    if (ball.xcor()>=330 and ball.distance(r_paddle)<=50 and ball.xcor()<360) or (ball.xcor()<=-330 and ball.distance(l_paddle)<=50 and ball.xcor()>-360):
        ball.x_move *=-1
        default_sleep *=0.9

    #missing shot
    if ball.xcor()>400:
        ball.goto(0,0)
        ball.x_move *=-1
        score.left_score_sum+=1
        score.update_score()
        default_sleep=0.1
    

    if ball.xcor()<-400:
        ball.goto(0,0)
        ball.x_move *=-1
        score.right_score_sum+=1
        score.update_score()
        default_sleep=0.1



screen.exitonclick()