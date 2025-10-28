import turtle as trtl 

trtl.addshape("football", (
    (-50, 0),    # Left end
    (-20, 25),   # Top-left curve
    (0, 30),     # Top point
    (20, 25),    # Top-right curve
    (50, 0),     # Right end
    (20, -25),   # Bottom-right curve
    (0, -30),    # Bottom point
    (-20, -25)   # Bottom-left curve
))

fb = trtl.Turtle(shape="football")
fb.setheading(90)

wn = trtl.Screen()
wn.mainloop()