import turtle as trtl

# Set up the screen
screen = trtl.Screen()
screen.bgcolor("black") # Set the background color to black


# Define custom defintion
trtl.addshape("star", ((0, 3), (2, 0), (4,-1), (2,-2), (3,-4), (1,-3), (-1,-3), (-3,-4), (-2,-2), (-4, -1), (-2, 0)))


# Draw a star
star = trtl.Turtle()
star.pensize(5) 
star.shape("star")
star.fillcolor("yellow")
star.penup()
star.goto(200, 0) # Position the star to the right
star.begin_fill()
star.stamp() # Stamp the star shape
star.end_fill()


# User Input
other_planets = trtl.textinput("Planets", "Do you want to see the planets? y/n")

# Define list
my_planets = ["Mercury", "Venus", "Earth", "Mars", "Jupter", "Saturn", "Uranus", "Neptune"] #planets list
my_planets_colors = ["lightgrey", "darkorange", "royalblue", "crimson", "goldenrod", "khaki", "lightskyblue", "dodgerblue"]


# Planet Radius
planets_radii = [10, 15, 15, 12, 25, 22, 20, 20]

# Draw Planets if user slects "y"
if other_planets.lower() == "y":
    tloc =150 # starting y-coordinates
    for i in range(len(my_planets)):
        planets = trtl.Turtle()
        planets.shape("star") # Changes pen to the stars
        planets.fillcolor(my_planets_colors)
        planets.penup()
        planets.goto(-150, tloc) # Position the planets
        planets.pendown()
        planets.begin_fill()
        planets.circle(20)
        planets.end_fill()
        tloc -= (planets_radii[i] * 2 + 10)
        
else:
 screen.bye()


#Keep it window open
screen = trtl.Screen()
screen.mainloop()