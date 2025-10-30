import turtle as trtl

# CORRECT WAY - Copy this exactly:
trtl.register_shape("car", ((-5,1),(-2,1),(-1,3),(3,3),(4,2),(4,1),(7,1),(7,-2),(4,-2),(4,-3),(3,-3),(3,-2),(-1,-2),(-1,-3),(-2,-3),(-3,-2),(-5,-2)))

# Create your car
car = trtl.Turtle()
car.shape("car")  # Now works!
car.color("red")
car.penup()

screen = trtl.Screen()
screen.mainloop()
