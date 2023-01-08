import turtle

# Constants
MOVE_DISTANCE = 10

class Paddle(turtle.Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x=position[0], y=position[1])
        
    def move_up(self):
        """Moves the paddle up."""
        
        self.sety(self.ycor() + MOVE_DISTANCE)

    def move_down(self):
        """Moves the paddle down."""
        
        self.sety(self.ycor() - MOVE_DISTANCE)
