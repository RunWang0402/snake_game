from turtle import Turtle, Screen
ALIGHMENT="center"
FONT=("Courier", 15, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.setposition(0,265)
        self.score=0
        with open("data.txt") as file:
            self.h_score = int(file.read())
        self.update_scoreboard()
        self.hideturtle()



    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.h_score}", False, ALIGHMENT, font=FONT)

    def update_score(self):
        self.score+=1
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME, OVER", False, ALIGHMENT, font=FONT)


    def reset(self):
        if self.score>self.h_score:
            self.h_score=self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.h_score}")
        self.score=0
        self.update_scoreboard()

