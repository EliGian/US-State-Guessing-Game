from turtle import Turtle

MAXIMUM_SCORE = 50

class Scoreboard(Turtle):
    
      def __init__(self):
            super().__init__()
            self.color("black")
            self.penup()
            self.hideturtle()
            self.score = 0
            self.UpdateScoreboard()

      
      def UpdateScoreboard(self) -> None:
            self.clear()
            self.goto(220,200)
            self.write(f"Current Score:{self.score}/{MAXIMUM_SCORE}",align="center", font=("Arial",14,"normal"))
        
    
      def IncreaseScore(self) -> None:
            self.score +=1