import turtle

# Constants
MOVE_DISTANCE = 10

class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.move_x = MOVE_DISTANCE
        self.move_y = MOVE_DISTANCE
        
    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        
        self.goto(x=new_x, y=new_y)
        
    def bounce_x(self):
        self.move_x *= -1
        
    def bounce_y(self):
        self.move_y *= -1
        
    def refresh(self):
        self.goto(x=0, y=0)
