import turtle
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# Window Setup
window = turtle.Screen()
window.setup(width=800, height=600)
window.bgcolor("black")
window.title("Pong")
window.tracer(0)

# Game Components
left_paddle = Paddle((-370, 0))
right_paddle = Paddle((370, 0))
ball = Ball()
scoreboard = Scoreboard()

window.listen()
window.onkey(key="Up", fun=left_paddle.move_up)
window.onkey(key="Down", fun=left_paddle.move_down)
window.onkey(key="w", fun=right_paddle.move_up)
window.onkey(key="s", fun=right_paddle.move_down)

playing = True

while playing:
    time.sleep(0.1) 
    window.update()  
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    if ball.distance(left_paddle) < 50 and ball.xcor() < -340 or ball.distance(right_paddle) < 50 and ball.xcor() > 340:
        ball.bounce_x()
    
    if ball.xcor() < -380:
        scoreboard.increase_score(2)
        ball.refresh()
    elif ball.xcor() > 380:
        scoreboard.increase_score(1)
        ball.refresh()
    
    ball.move() 

window.mainloop()
