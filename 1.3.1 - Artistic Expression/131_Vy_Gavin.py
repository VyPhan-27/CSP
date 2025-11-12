import turtle as trtl 
import random as rand

# TODO Title Screen
title = trtl.Turtle()
title.pensize(1)
title.penup()
title.goto(0, -110)
title.pencolor("grey")
title.write("Hello!, Welcome to our Game", align='center', font=("Arial", 60, "normal"))
title.goto(0, -160)
title.pencolor("red")
title.write("Press SPACE, to start the game", align='center', font=("Arial", 50, "normal"))
title.hideturtle()

# Background
screen = trtl.Screen()
screen.setup(width=1000, height=570)
screen.bgpic("surface_water.gif")
# Message

# TODO Start the game
def start_game():
    title.clear()
    

# Begining to Start
screen.listen()
screen.onkeypress(start_game, "space")

wn = trtl.Screen()
wn.mainloop()