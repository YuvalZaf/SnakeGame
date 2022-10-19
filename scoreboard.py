from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):  # constructor
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.write(f"score: {self.score}", False, "center", ('Arial', 15, 'normal'))

    def point(self):  # adds a point to the player score
        self.score += 1
        self.clear()
        self.write(f"score: {self.score}", False, "center", ('Arial', 15, 'normal'))

    def game_over(self):  # if game is over
        over = Turtle()
        over.color("white")
        over.hideturtle()
        over.penup()
        over.goto(0, 0)
        over.write(f"GAME OVER.", False, "center", ('Arial', 15, 'normal'))
