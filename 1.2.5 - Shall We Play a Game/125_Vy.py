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

# Create an list
cars = ["cars1","cars2","cars3","cars4","cars5","cars6"]
cars_color = ["red","blue","green","black","grey","white"]
# Custom Turtle

# TODO Customize Turtle 

# TODO Create an timer 

# TODO Win or Lose Screen

# TODO Players Scores and Difficulty level chosen




wn = trtl.Screen()
wn.mainloop()