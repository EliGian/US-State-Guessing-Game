from turtle import Turtle, Screen


class Printer(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.hideturtle()

    def DrawNameOnMap(self,state_name:str,coordinates:tuple)->None:
        printer = Printer()
        printer.goto(coordinates[0],coordinates[1])
        printer.write(state_name,align="center", font=("Arial",14,"normal"))
       