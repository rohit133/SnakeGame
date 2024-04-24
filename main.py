import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
 
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game") 
screen.tracer(0)

jim =Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(jim.up,"Up")
screen.onkey(jim.down,"Down")
screen.onkey(jim.left,"Left")
screen.onkey(jim.right,"Right")



def play_game():

    """Entier gaming calulations and combination is done here """
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        jim.move()
        

        # Deteching collision with the food
        if jim.head.distance(food) < 15:
            food.refresh()
            jim.extend()
            score.increase_score()

        # Detecting collision with the Wall
        if jim.head.xcor() > 290 or jim.head.xcor() < -290 or jim.head.ycor() > 290 or jim.head.ycor() < -290:
            score.reset_game()
            jim.reset()
        
        # Detecting Collision with Tail       
        # if head of the sanke collied with any segment of the snake body then 
        # trigger the game over sequence
        for seg in jim.segment[1:]:
            if jim.head.distance(seg) < 10:
                score.reset_game()
                jim.reset()


play_game()




screen.exitonclick()
