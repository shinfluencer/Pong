import turtle

# Constants
ALIGN = "center"
FONT_CONFIG = ("Courier", 20, "normal")

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=260)
        self.player_1_score = 0
        self.player_2_score = 0
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write(arg=f"Player 1: {self.player_1_score} | Player 2: {self.player_2_score}", move=False, align=ALIGN, font=FONT_CONFIG)
    
    def increase_score(self, player):
        if player == 1:
            self.player_1_score += 1
        else:
            self.player_2_score += 2
        
        self.update_score()
