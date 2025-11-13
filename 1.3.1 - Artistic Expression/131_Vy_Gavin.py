import turtle as trtl 
import random as rand

# Background
screen = trtl.Screen()
screen.setup(width=1000, height=570)
screen.bgpic("surface_water.gif")
screen.tracer(0)

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

# Boat images
boat = trtl.Turtle()
screen.addshape("boat.gif")
boat.shape("boat.gif")
boat.penup()
boat.goto(-400, -200)

# Island images
island = trtl.Turtle()
screen.addshape("island.gif")
island.shape("island.gif")
island.penup()
island.goto(400, -200)

# Game State
game_started = False
score = 0
target_score = 8
boat_speed = 70

# TODO User input Question 
prompt = trtl.Turtle()
prompt.hideturtle()
prompt.penup()

used_questions = set() # Keep on track with the Question

def generate_question():
    global used_questions
    attempts = 0
    while attempts < 50:                    
        a = rand.randint(1, 15)
        b = rand.randint(1, 15)
        op = rand.choice(['+', '-'])

        # Subtraction
        if op == '-' and a < b:
            a, b = b, a                    

        answer = a + b if op == '+' else a - b
        q_str = f"{a} {op} {b}"

        if q_str not in used_questions:
            used_questions.add(q_str)
            return f"{a} {op} {b} = ?", answer

        attempts += 1

    return "5 + 3 = ?", 8

# Shows the Question 
current_question = ""
current_answer = 0

def show_question():
    global current_question, current_answer
    prompt.clear()
    prompt.goto(0, 200)
    prompt.write("Solve to move the boat!", align='center',
                 font=("Arial", 30, "bold"))
    current_question, current_answer = generate_question()
    prompt.goto(0, 150)
    prompt.write(current_question, align='center',
                 font=("Arial", 40, "normal"))
    prompt.goto(0, 100)
    prompt.write("Type answer → OK", align='center',
                 font=("Arial", 20, "italic"))
    screen.update()

# Ask the player the Question
def ask_for_answer():
    user = screen.textinput("Math Challenge", current_question)
    if user is not None:
        check_answer(user.strip())
    else:
        screen.ontimer(ask_for_answer, 500)
    
# TODO Right/Correct Messages
def check_answer(user_input):
    global score
    try:
        if int(user_input) == current_answer:
            move_boat()
            feedback("Great Job!", "green")
            score += 1
            if score >= target_score:
                screen.ontimer(win_screen, 1200)
            else:
                screen.ontimer(ask_for_answer, 1200)
        else:
            feedback("Keep Trying!", "red")
            screen.ontimer(ask_for_answer, 1200)
    except ValueError:
        feedback("Numbers only!", "orange")
        screen.ontimer(ask_for_answer, 1200)

def move_boat():
    x, y = boat.position()
    new_x = min(x + boat_speed, 500)
    boat.goto(new_x, y)
    screen.update()
# Feedback towards the Answers
def feedback(msg, color):
    t = trtl.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(0, 50)
    t.pencolor(color)
    t.write(msg, align='center', font=("Arial", 36, "bold"))
    screen.ontimer(t.clear, 1500)
# TODO Animate Boat

# TODO Win Screen 
def win_screen():
    screen.clear()
    screen.bgcolor("skyblue")
    win = trtl.Turtle()
    win.hideturtle()
    win.penup()
    win.goto(0, 80)
    win.pencolor("gold")
    win.write("YOU WIN!", align='center', font=("Arial", 80, "bold"))
    win.goto(0, 0)
    win.pencolor("navy")
    win.write(f"Score: {score}/{target_score}", align='center',
              font=("Arial", 40, "normal"))
    win.goto(0, -60)
    win.write("Boat reached the island!", align='center',
              font=("Arial", 30, "normal"))

# Start the Game
def start_game():
    global game_started, score, used_questions
    if not game_started:
        game_started = True
        title.clear()
        boat.goto(-400, -200)
        score = 0
        used_questions = set()
        show_question()
        screen.ontimer(ask_for_answer, 1500)

# Begining to Start
screen.onkeypress(start_game, "space")
screen.listen()

screen.mainloop()