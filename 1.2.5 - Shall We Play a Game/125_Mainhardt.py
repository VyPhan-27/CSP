import turtle as trtl
import random as rand

# Title Screen
title = trtl.Turtle()
title.pensize(5)
title.penup()
title.goto(0,-110)
title.write("Street Crossing!", align='center', font=("Arial", 60, "normal"))

# Start prompt
prompt = trtl.Turtle()
prompt.hideturtle()
prompt.penup()
prompt.goto(0, -180)
prompt.color("grey")
prompt.write("Press SPACE to start", align='center', font=("Arial", 60, "normal"))

# Screen setup
screen = trtl.Screen()
screen.setup(width=850, height=740)
screen.title("Street Crossing!")
screen.bgpic("street.gif")

# Car lanes
car_lane = [270, 220, 70, 10, -140, -190]

# Custom car shape
trtl.register_shape("car", ((-5,1),(-2,1),(-1,3),(3,3),(4,2),(4,1),(7,1),
                           (7,-2),(4,-2),(4,-3),(3,-3),(3,-2),(-1,-2),
                           (-1,-3),(-2,-3),(-3,-2),(-5,-2)))

# Car colors
default_cars_color = ["red","blue","green","black","grey","white"]
cars = []

# Create 6 cars
for i in range(6):
    car_set = trtl.Turtle()
    car_set.speed(0)
    car_set.shape("car")
    car_set.shapesize(10)
    car_set.right(270)
    car_set.color(default_cars_color[i])
    car_set.penup()
    car_set.goto(450, car_lane[i])
    car_set.dx = rand.randint(8, 16)
    cars.append(car_set)

# Player customization
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
    col = None
    shp = None
    if custom and custom.lower() == "custom":
        col = screen.textinput("Color", "Enter a color (e.g. red, blue, lime):")
        if col:
            color = col.lower()
        shp = screen.textinput("Shape","Enter shape (turtle, arrow, circle, square, triangle):")
        valid = ["turtle", "arrow", "circle", "square", "triangle", "classic"]
        if shp and shp.lower() in valid:
            shape = shp.lower()

    return color, shape

# ========================================
# TIMER (counts UP)
# ========================================
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

# ========================================
# PLAYER MOVEMENT WITH ARROW KEYS
# ========================================
player = None
GRID_SIZE = 30  # Move in 30px steps

def move_up():
    if player.ycor() < 320:
        player.sety(player.ycor() + GRID_SIZE)

def move_down():
    if player.ycor() > -320:
        player.sety(player.ycor() - GRID_SIZE)

def move_left():
    if player.xcor() > -400:
        player.setx(player.xcor() - GRID_SIZE)

def move_right():
    if player.xcor() < 400:
        player.setx(player.xcor() + GRID_SIZE)

# ========================================
# START GAME ON SPACE
# ========================================
def start_game():
    title.clear()
    prompt.clear()
    player_color, player_shape = ask_player()
    if player_color is None:
        return
    
    global player
    player = trtl.Turtle()
    player.shape(player_shape)
    player.color(player_color)
    player.penup()
    player.speed(0)
    player.goto(0, -300)
    
    # Start timer
    start_timer()

    # Bind arrow keys
    screen.onkey(move_up, "Up")
    screen.onkey(move_down, "Down")
    screen.onkey(move_left, "Left")
    screen.onkey(move_right, "Right")
    screen.listen()

# ========================================
# CAR MOVEMENT LOOP
# ========================================
def move_cars():
    for car in cars:
        if isinstance(car, trtl.Turtle):
            car.setx(car.xcor() + car.dx)
            if car.xcor() > 500:
                car.goto(-500, car.ycor())
    screen.update()
    screen.ontimer(move_cars, 50)

# ========================================
# START EVERYTHING
# ========================================
screen.listen()
screen.onkey(start_game, "space")
screen.tracer(0)
move_cars()
screen.tracer(1)

screen.mainloop()