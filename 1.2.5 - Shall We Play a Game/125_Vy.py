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
# Spawn in Cars
def spawn_title_cars():
    global cars
    cars = []
    for i in range(6):
        car = trtl.Turtle()
        car.speed(0)
        car.shape("car")
        car.shapesize(10)
        car.right(270)
        car.color(default_cars_color[i])
        car.penup()
        car.goto(450, car_lane[i])

        base = rand.randint(8, 16)
        car.dx = base * 1.0  # slow speed for title screen
        cars.append(car)
    
    screen.update()

# Move the Cars
def move_cars():
    for car in cars:
        if isinstance(car, trtl.Turtle):
            car.setx(car.xcor() + car.dx)
            if car.xcor() > 500:
                car.goto(-500, car.ycor())
    screen.ontimer(move_cars, 50)
# TODO Choice of Customize Turtle 
def ask_player():
    while True:
        response = screen.textinput("Start", "Type yes to play or no:")
        if response is None:
            screen.bye()
            return None, None
        if response.strip().lower() in ("yes","y","ok"):
            break
        elif response.strip().lower() in ("no","n"):
            screen.textinput("Try Again",
                "You said no. Let's try again!\nType again to restart.")
        else:
            screen.textinput("Invalid", "Please type yes or no.")

    custom = screen.textinput("Customize", "Type 'custom' or default:").strip()
    color = "lime"
    shape = "turtle"

    if custom and custom.lower() == "custom":
        col = screen.textinput("Color",
                "Enter a color (e.g. red, blue, lime):")
        if col:
            color = col.lower()
        shp = screen.textinput("Shape",
                "Enter shape (turtle, arrow, circle, square, triangle, classic):")
        valid = ["turtle","arrow","circle","square","triangle","classic"]
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
        timer_turtle.write(f"Time: {elapsed_time}", align="right", font=("Arial", 24, "bold"))
        elapsed_time += 1
        screen.ontimer(update_timer, 1000)

def stop_timer():
    global timer_active
    timer_active = False

# Start game on space
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
    player.speed(100)
    player.left(90)
    player.penup()
    player.speed(0)
    player.goto(0, -300)
    
    # begin timer
    start_timer()
    #Bind Keys 
    screen.onkey(move_up, "Up")
    screen.onkey(move_down, "Down")
    screen.onkey(move_left, "Left")
    screen.onkey(move_right, "Right")
    screen.listen()
# Create Bind Keys
player = None
GRID_SIZE = 30

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
# Start the game
screen.listen()
screen.onkeypress(start_game,"space")
move_cars()
screen.tracer(0)
# TODO Win or Lose Screen
def win_game():
    stop_timer()
    screen.onkey(None, "Up"); screen.onkey(None, "Down")
    screen.onkey(None, "Left"); screen.onkey(None, "Right")
    player.hideturtle()

    win = trtl.Turtle()
    win.hideturtle()
    win.goto(0, 0)
    win.write(f"You WIN!\nTime: {elapsed_time}s",
              align="center", font=("Arial", 48, "bold"))
    screen.update()
    screen.ontimer(screen.bye, 4000)
def lose_game():
    stop_timer()
    screen.onkey(None, "Up"); screen.onkey(None, "Down")


# TODO Players Scores and Difficulty level chosen

wn = trtl.Screen()
wn.mainloop()