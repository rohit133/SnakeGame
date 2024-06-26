from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as game_data:
            self.high_score = int(game_data.read())
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 260)
        self.update_scoreboad()

     
    def update_scoreboad(self):
        self.clear()
        self.write(f"Score = {self.score} High Score = {self.high_score}", align=ALIGNMENT, font=FONT)



    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score 
            with open("data.txt", mode="w") as game_data:
                game_data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboad()

    # def game_over(self):
    #     self.goto(0, 0) 
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

         

    def increase_score(self):
        self.score += 1
        self.update_scoreboad()
