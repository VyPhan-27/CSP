# --------------------------------------------------------------
#  Street Crossing! – FULLY FIXED & COMPLETE
#  Street Crossing! – Cars on Title Screen + Speed Change
# --------------------------------------------------------------
import turtle as trtl
import random as rand

# ---------- 1. Title screen ----------
title = trtl.Turtle()
title.pensize(5)
title.penup()
title.goto(0, -110)
title.write("Street Crossing!", align='center', font=("Arial", 60, "normal"))

prompt = trtl.Turtle()
prompt.hideturtle()
prompt.penup()
prompt.goto(0, -180)
prompt.color("grey")
prompt.write("Press SPACE to start", align='center', font=("Arial", 60, "normal"))

# ---------- 2. Window & background ----------
screen = trtl.Screen()
screen.setup(width=850, height=740)
screen.title("Street Crossing!")
screen.bgpic("street.gif")          # <-- make sure street.gif is in the same folder
screen.bgpic("street.gif")

# ---------- 3. Car data ----------
car_lane = [270, 220, 70, 10, -140, -190]
trtl.register_shape("car",
    ((-5,1),(-2,1),(-1,3),(3,3),(4,2),(4,1),(7,1),(7,-2),
     (4,-2),(4,-3),(3,-3),(3,-2),(-1,-2),(-1,-3),(-2,-3),(-3,-2),(-5,-2)))

default_colors = ["red","blue","green","black","grey","white"]
cars = []

# ---------- 4. Player movement ----------
GRID_SIZE = 30
player = None

def move_up():
    if player and player.ycor() < 320:
        player.sety(player.ycor() + GRID_SIZE)
        check_win()

def move_down():
    if player and player.ycor() > -320:
        player.sety(player.ycor() - GRID_SIZE)

def move_left():
    if player and player.xcor() > -400:
        player.setx(player.xcor() - GRID_SIZE)

def move_right():
    if player and player.xcor() < 400:
        player.setx(player.xcor() + GRID_SIZE)

# ---------- 5. Timer ----------
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
        timer_turtle.write(f"Time: {elapsed_time}s", align="center",
                           font=("Arial", 24, "bold"))
        elapsed_time += 1
        screen.ontimer(update_timer, 1000)

def stop_timer():
    global timer_active
    timer_active = False

# ---------- 6. Player customisation ----------
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

# ---------- 7. Difficulty ----------
speed_multiplier = 1.0

def choose_difficulty():
    global speed_multiplier
    while True:
        diff = screen.textinput("Difficulty",
                "Choose: easy / medium / hard").strip().lower()
        if diff in ("easy", "e"):
            speed_multiplier = 1.5
            speed_multiplier = 2.0
            break
        elif diff in ("medium", "m"):
            speed_multiplier = 2.0
            speed_multiplier = 2.5
            break
        elif diff in ("hard", "h"):
            speed_multiplier = 2.5
            speed_multiplier = 3.0
            break
        else:
            screen.textinput("Oops", "Please type easy, medium or hard.")
    
    # **NEW: UPDATE CAR SPEEDS when difficulty is chosen**
    for car in cars:
        base = rand.randint(8, 16)
        car.dx = base * speed_multiplier
    screen.update()

# ---------- 8. Create cars ----------
def spawn_cars():
# ---------- 8. Create cars (for title screen) ----------
def spawn_title_cars():
    global cars
    cars = []
    for i in range(6):
        car = trtl.Turtle()
        car.speed(0)
        car.shape("car")
        car.shapesize(10)
        car.right(270)
        car.color(default_colors[i])
        car.penup()
        car.goto(450, car_lane[i])

        base = rand.randint(8, 16)
        car.dx = base * speed_multiplier
        car.dx = base * 1.0  # slow speed for title screen
        cars.append(car)

    screen.update()          # SHOW CARS
    screen.update()

# ---------- 9. Car movement ----------
def move_cars():
    for car in cars:
        car.setx(car.xcor() + car.dx)
        if car.xcor() > 500:
            car.goto(-500, car.ycor())
    screen.update()          # UPDATE SCREEN
    screen.update()
    screen.ontimer(move_cars, 50)

# ---------- 10. Collision detection ----------
def check_collision():
    if not player or not timer_active:
        return
    px, py = player.xcor(), player.ycor()
    for car in cars:
        if abs(px - car.xcor()) < 55 and abs(py - car.ycor()) < 55:
            lose_game()
            return

# ---------- 11. Win / Lose screens ----------
def win_game():
    stop_timer()
    screen.onkey(None, "Up"); screen.onkey(None, "Down")
    screen.onkey(None, "Left"); screen.onkey(None, "Right")
    player.hideturtle()

    win = trtl.Turtle()
    win.hideturtle()
    win.penup()
    win.goto(0, 0)
    win.write(f"You WIN!\nTime: {elapsed_time}s",
              align="center", font=("Arial", 48, "bold"))
    screen.update()
    screen.ontimer(screen.bye, 4000)

def lose_game():
    stop_timer()
    screen.onkey(None, "Up"); screen.onkey(None, "Down")
    screen.onkey(None, "Left"); screen.onkey(None, "Right")
    player.hideturtle()

    lose = trtl.Turtle()
    lose.hideturtle()
    lose.penup()
    lose.goto(0, 0)
    lose.pencolor("grey")
    lose.write("GAME OVER\nHit by a car!",
               align="center", font=("Arial", 48, "bold"))
    screen.update()
    screen.ontimer(screen.bye, 3000)

def check_win():
    if player and player.ycor() >= 250:
        win_game()

# ---------- 12. Main start routine ----------
def start_game():
    global player

    title.clear()
    prompt.clear()

    player_color, player_shape = ask_player()
    if player_color is None:
        return
    choose_difficulty()
    
    choose_difficulty()  # Cars speed changes HERE!

    player = trtl.Turtle()
    player.shape(player_shape)
    player.color(player_color)
    player.penup()
    player.speed(0)
    player.goto(0, -300)

    screen.update()          # SHOW PLAYER
    screen.update()

    spawn_cars()
    start_timer()
    move_cars()

    # Bind keys
    screen.onkey(move_up,    "Up")
    screen.onkey(move_down,  "Down")
    screen.onkey(move_left,  "Left")
    screen.onkey(move_right, "Right")
    screen.listen()

    # Collision loop
    def collision_loop():
        if timer_active:
            check_collision()
            screen.update()
            screen.ontimer(collision_loop, 50)
    collision_loop()

# ---------- 13. Kick-off ----------
screen.listen()
screen.onkeypress(start_game, "space")
screen.tracer(0)          # SMOOTH ANIMATION

# **NEW: Spawn cars for title screen**
spawn_title_cars()
move_cars()  # Start car movement immediately

screen.tracer(0)
screen.mainloop()