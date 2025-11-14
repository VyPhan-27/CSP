import turtle as trtl 
import random as rand

# Background
screen = trtl.Screen()
screen.setup(width=1000, height=570)
screen.bgpic("surface_water.gif")
screen.tracer(0)

# Title Screen
title = trtl.Turtle()
title.hideturtle()
title.penup()
title.goto(0, -110)
title.pencolor("grey")
title.write("Hello!, Welcome to our Game", align='center', font=("Arial", 60, "normal"))
title.goto(0, -160)
title.pencolor("red")
title.write("Press SPACE to start the game", align='center', font=("Arial", 50, "normal"))

# Boat
boat = trtl.Turtle()
screen.addshape("boat.gif")
boat.shape("boat.gif")
boat.penup()
boat.goto(-400, -200)

# Island
island = trtl.Turtle()
try:
    screen.addshape("island.gif")
    island.shape("island.gif")
except:
    island.shape("square")
screen.addshape("island.gif")
island.shape("island.gif")
island.penup()
island.goto(400, -200)
island.shapesize(4, 6)

# Wind Effect Turtle
wind = trtl.Turtle()
try:
    screen.addshape("wind.gif")
    wind.shape("wind.gif")
except:
    wind.shape("triangle")
wind.penup()
wind.hideturtle()

# Game State
game_started = False
score = 0
target_score = 8
boat_speed = 70
wind_pushback = 60  # How far wind pushes back

# List to store questions and answers
question_bank = []
used_questions = set()

def generate_question():
    global used_questions, question_bank
    attempts = 0
    while attempts < 50:
        a = rand.randint(1, 15)
        b = rand.randint(1, 15)
        op = rand.choice(['+', '-'])
        if op == '-' and a < b:
            a, b = b, a
        answer = a + b if op == '+' else a - b
        q_str = f"{a} {op} {b}"

        if q_str not in used_questions:
            used_questions.add(q_str)
            full_q = f"{a} {op} {b} = ?"
            question_bank.append([full_q, answer])
            return full_q, answer
        attempts += 1

    fallback = "7 + 5 = ?"
    question_bank.append([fallback, 12])
    return fallback, 12

# Show question
prompt = trtl.Turtle()
prompt.hideturtle()
prompt.penup()

current_question = ""
current_answer = 0

def show_question():
    global current_question, current_answer
    prompt.clear()
    prompt.goto(0, 180)
    prompt.pencolor("black")
    prompt.write("Solve to move the boat!", align='center',
                 font=("Arial", 30, "bold"))
    current_question, current_answer = generate_question()
    prompt.goto(0, 130)
    prompt.write(current_question, align='center',
                 font=("Arial", 40, "normal"))
    prompt.goto(0, 90)
    prompt.write("Type answer to OK", align='center',
                 font=("Arial", 20, "italic"))
    screen.update()

# Ask player
def ask_for_answer():
    user = screen.textinput("Math Challenge", current_question)
    if user is not None:
        check_answer(user.strip())
    else:
        screen.ontimer(ask_for_answer, 500)

# Check answer
def check_answer(user_input):
    global score
    try:
        if int(user_input) == current_answer:
            move_boat()
            feedback("Great Job!", "lime")
            score += 1
            if score >= target_score:
                screen.ontimer(win_screen, 1200)
            else:
                screen.ontimer(show_question, 1500)
                screen.ontimer(ask_for_answer, 2000)
        else:
            wind_push()
            feedback("Keep Trying!", "red")
            screen.ontimer(ask_for_answer, 2000)
    except ValueError:
        feedback("Numbers only!", "orange")
        screen.ontimer(ask_for_answer, 1200)

# Move boat forward
def move_boat():
    x, y = boat.position()
    new_x = min(x + boat_speed, 350)
    boat.goto(new_x, y)
    screen.update()

# WIND PUSHBACK EFFECT
def wind_push():
    x, y = boat.position()
    new_x = max(x - wind_pushback, -400)  # Don't go past start
    boat.goto(new_x, y)
    
    # Show wind animation
    wind.goto(x + 100, y + 70)
    wind.showturtle()
    wind.stamp()
    screen.ontimer(wind.hideturtle, 800)
    wind.clear()
    screen.update()

# Feedback
def feedback(msg, color):
    t = trtl.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(0, 50)
    t.pencolor(color)
    t.write(msg, align='center', font=("Arial", 36, "bold"))
    screen.ontimer(t.clear, 1500)
    screen.update()

# Win Screen
def win_screen():
    screen.clear()
    screen.bgcolor("skyblue")

    win = trtl.Turtle()
    win.hideturtle()
    win.penup()

    win.goto(0, 180)
    win.pencolor("gold")
    win.write("YOU WIN!", align='center', font=("Arial", 70, "bold"))

    win.goto(0, 120)
    win.pencolor("navy")
    win.write(f"Score: {score}/{target_score}", align='center',
              font=("Arial", 40, "normal"))

    # Show all questions and answers
    win.goto(-400, 80)
    win.pencolor("black")
    win.write("All Equations & Answers:", align="left", font=("Arial", 24, "bold"))

    y_pos = 40
    for i, (q, ans) in enumerate(question_bank):
        win.goto(-400, y_pos)
        win.write(f"{i+1}. {q} {ans}", align="left", font=("Arial", 20, "normal"))
        y_pos -= 30
        if y_pos < -250:
            break

    win.goto(0, -200)
    win.write("Boat reached the island!", align='center',
              font=("Arial", 28, "italic"))
    win.pencolor("red")
    win.goto(400, -60)
    win.write("You did an Amazing Job", align="right", font=("Arial", 24, "bold"))
    win.goto(400, -80)
    win.write("Great Job! and also know that we here for you!", align="right", font=("Arial", 24, "bold"))

# Start game
def start_game():
    global game_started, score, used_questions, question_bank
    if not game_started:
        game_started = True
        title.clear()
        boat.goto(-400, -200)
        wind.hideturtle()
        score = 0
        used_questions = set()
        question_bank = []
        show_question()
        screen.ontimer(ask_for_answer, 1500)
        screen.update()

# Key binding
screen.onkeypress(start_game, "space")
screen.listen()

screen.mainloop()