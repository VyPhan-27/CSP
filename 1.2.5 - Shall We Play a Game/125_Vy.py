import turtle as trtl
import random as rand

# TODO create an Title Screen
title = trtl.Turtle()
title.pensize(5)
title.penup()
title.goto(0,-110)
title.write("Street Crossing!", align='center',  font=("Arial", 60, "normal"))
# Beginning the game
prompt = trtl.Turtle()
prompt.hideturtle()
prompt.penup()
prompt.goto(0, -180)
prompt.color("grey")
prompt.write("Press SPACE to start", align='center',  font=("Arial", 60, "normal"))
# Create an street background
screen = trtl.Screen()
screen.setup(width=850, height=740)
screen.title("Street Crossing!")
screen.bgpic("street.gif")
# TODO Create Position for each cars
car_lane = [270, 220, 70, 10, -140, -190]
# Custom Turtle
trtl.register_shape("car", ((-5,1),(-2,1),(-1,3),(3,3),(4,2),(4,1),(7,1),(7,-2),(4,-2),(4,-3),(3,-3),(3,-2),(-1,-2),(-1,-3),(-2,-3),(-3,-2),(-5,-2)))
# Create an list
cars = ["cars1","cars2","cars3","cars4","cars5","cars6"]
default_cars_color = ["red","blue","green","black","grey","white"]
# Posistion Cars correctly
for i in range(6):
    car_set = trtl.Turtle()
    car_set.speed(100)
    car_set.shape("car")
    car_set.shapesize(10)
    car_set.right(270)
    car_set.color(default_cars_color[i])
    car_set.penup()
    car_set.speed(0)
    car_set.goto(450, car_lane[i])
    car_set.dx = rand.randint(8, 16)
    cars.append(car_set)
# TODO Choice of Customize Turtle 
def ask_player():
    while True:
       response = screen.textinput("Start", "Type YES to play:")
       if response is None:
           screen.bye()
           return None, None
       if response.strip().lower() in ["yes", "y", "ok"]:
           break
       elif response.strip().lower() in ["no", "n"]:
           screen.textinput("Try Again", "You said NO. Let's try again!\nType YES to play.")
       else:
            screen.textinput("Invalid", "Please type YES or NO.")

    custom = screen.textinput("Customize", "Type 'custom' or leave blank:")
    color = "lime"
    shape = "turtle"
    if custom and custom.lower() == "custom":
      col = screen.textinput("Color", "Enter a color (e.g. red, blue, lime):")
    if col:
      color = col.lower()
    shp = screen.textinput("Shape","Enter shape (turtle, arrow, circle, square, triangle):")
    valid = ["turtle", "arrow", "circle", "square", "triangle", "classic"]
    if shp and shp.lower() in valid:
      shape = shp.lower()

    return color, shape
# TODO Create an timer
elapsed_time = 0
timer_turtle = None
timer_active = False

def start_timer():
    global timer_turtle, timer_active, elapsed_time
    timer_active = True
    elapsed_time = 0
    timer_turtle = trtl.Turtle()
    timer_turtle.hideturtle()
    timer_turtle.penup()
    timer_turtle.goto(0, 310)
    update_timer()

def update_timer():
    global elapsed_time
    if timer_active:
        timer_turtle.clear()
        timer_turtle.write(f"Time: {elapsed_time}", align="center", font=("Arial", 24, "bold"))
        elapsed_time += 1
        screen.ontimer(update_timer, 1000)

def stop_timer():
    global timer_active
    timer_active = False
# TODO Win or Lose Screen

# TODO Players Scores and Difficulty level chosen




wn = trtl.Screen()
wn.mainloop()