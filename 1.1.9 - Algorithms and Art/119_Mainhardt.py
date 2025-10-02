import turtle as trtl

# Set up the screen
screen = trtl.Screen()
screen.bgcolor("black")  # Set background color to black

# Define custom star shape
trtl.addshape("star", ((0, 3), (2, 0), (4, -1), (2, -2), (3, -4), (1, -3), (-1, -3), (-3, -4), (-2, -2), (-4, -1), (-2, 0)))

# Draw a star (e.g., representing the sun)
star = trtl.Turtle()
star.pensize(4)
star.shape("star")
star.fillcolor("yellow")
star.penup()
star.goto(200, 0)  # Position the star to the right
star.begin_fill()
star.stamp()  # Stamp the star shape
star.end_fill()

# User input
other_planets = trtl.textinput("Planets", "Do you want to see the planets? y/n")

# Planet and color lists
my_planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
my_planets_colors = ["lightgrey", "darkorange", "royalblue", "crimson", "goldenrod", "khaki", "lightskyblue", "dodgerblue"]


# Plant radius
planet_radii = [10, 15, 15, 15, 26, 24, 20, 20]

# Draw planets if user selects 'y'
if other_planets.lower() == "y":
    tloc = 250  # Starting y-coordinate
    for i in range(len(my_planets)):
        planet = trtl.Turtle()
        planet.shape("star")  # Use circle for planets
        planet.fillcolor(my_planets_colors[i]) # Set color from list
        planet.penup()
        planet.goto(-200, tloc) # Position planet
        planet.setheading(0)
        planet.pendown()
        planet.begin_fill()
        planet.circle(planet_radii[i])  # Smaller radius for visibility
        planet.end_fill()
        tloc -= (planet_radii[i] * 4 + 9)  # Move down for next planet
else:
    exit()



# Keep the window open
screen.mainloop()