import turtle as trtl
import random as rand

# TODO create an Title Screen
title = trtl.Turtle()
title.pensize(5)
title.penup()
title.goto(0,-110)
title.write("Street Crossing!", align='center',  font=("Arial", 60, "normal"))
# Create an street background
screen = trtl.Screen()
screen.setup(width=850, height=740)
screen.title("Street Crossing!")
screen.bgpic("street.gif")
# TODO Create Position for each cars
starting_position = [140, 110, 80, 50, 20, 0]
# Create an list
cars = ["cars1","cars2","cars3","cars4","cars5","cars6"]
default_cars_color = ["red","blue","green","black","grey","white"]
# Custom Turtle
car = ((-5,1),(-2,1),(-1,3),(3,3),(4,2),(4,1),(7,1),(7,-2),(4,-2),(4,-3),(3,-3),(3,-2),(-1,-2),(-1,-3),(-2,-3),(-3,-2),(-5,-2))
# TODO Choice of Customize Turtle 
customize = trtl.textinput("Start the game?","yes/no?")
customize = trtl.textinput("Customize turtle", "Customize or Default?")
customize = trtl.textinput("Turtle Colors", "Pick an Color")
customize = trtl.textinput("Turtle Shapes", "Choose an Shape in Python")
# TODO Create an timer

# TODO Win or Lose Screen

# TODO Players Scores and Difficulty level chosen




wn = trtl.Screen()
wn.mainloop()