from turtle import Screen, Turtle
from scoreboard import Scoreboard
from csvhandler import CsvHandler
from printer import Printer

main_screen = Screen()
scoreboard = Scoreboard()
csvhandler = CsvHandler()
inputbar = Turtle()
printer = Printer()

main_screen.setup(width=725,height=491)
main_screen.bgpic("blank_states_img.gif")

Game_is_on = True

while Game_is_on:
   scoreboard.UpdateScoreboard()
   input_user = main_screen.textinput("US State Game","Tell me a name of a US State")
   coordinates = csvhandler.CheckInput(input_user)
   if(coordinates != (0,0)):
      scoreboard.IncreaseScore()
      printer.DrawNameOnMap(input_user,coordinates)



main_screen.exitonclick()