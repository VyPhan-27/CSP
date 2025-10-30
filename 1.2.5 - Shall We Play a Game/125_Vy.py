import turtle as trtl
import random as rand

# TODO create an Title Screen
title = trtl.Turtle()
title.pensize(5)
title.penup()
title.goto(0,-110)
title.write("Street Crossing!", align='center',  font=("Arial", 60, "normal"))
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
# Funcation of looping
def move_cars():
    for car in cars:
        # Move right
        car.setx(car.xcor() + car.dx)

        # Loop back to left when off-screen
        if car.xcor() > 500:
            car.goto(-500, car.ycor())

    # Repeat every 30ms (~33 FPS)
    screen.ontimer(move_cars, 30)

# TODO Choice of Customize Turtle 

# TODO Create an timer

# TODO Win or Lose Screen

# TODO Players Scores and Difficulty level chosen




wn = trtl.Screen()
wn.mainloop()