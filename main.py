from turtle import Turtle, Screen
from paddel import Paddles
from ball import Balls
from score_board import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width= 800, height= 600)
screen.title("PONG")
screen.tracer(0)


r_paddle = Paddles((350, 0))
l_paddle = Paddles((-350, 0))
ball = Balls()
score = ScoreBoard()


screen.listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")



is_playing = True

while is_playing:
    time.sleep(.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bouncex()

    if ball.xcor() > 380:
        ball.reset_ball()
        score.l_increase()

    if ball.xcor() < -380:
        ball.reset_ball()


screen.exitonclick()
