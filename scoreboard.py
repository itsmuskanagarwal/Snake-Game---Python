from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update()

    def update(self):
        self.write(f"Score: {self.score}", align="center", font=("Calibri", 20, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.clear()
        self.write(f"GAME OVER", align="center", font=("Calibri", 24, "normal"))
        self.goto(self.xcor(), self.ycor() -  50 )
        self.write(f"Score: {self.score}", align="center", font=("Calibri", 20, "normal"))

    def increase(self):
        self.score += 1
        self.clear()
        self.update()





