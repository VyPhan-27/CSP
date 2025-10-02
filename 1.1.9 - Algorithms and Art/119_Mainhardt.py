import turtle as trtl

# Set up the screen
screen = trtl.Screen()
screen.bgcolor("black")  # Set background color to black

# Define custom star shape
trtl.addshape("star", ((0, 3), (2, 0), (4, -1), (2, -2), (3, -4), (1, -3), (-1, -3), (-3, -4), (-2, -2), (-4, -1), (-2, 0)))

# Draw a star (e.g., representing the sun)
sun = trtl.Turtle()
sun.pensize(4)
sun.shape("star")
sun.fillcolor("yellow")
sun.penup()
sun.goto(200, 0)  # Position the star to the right
sun.begin_fill()
sun.stamp()  # Stamp the star shape
sun.end_fill()

# User input
other_planets = trtl.textinput("Planets", "Do you want to see the planets? y/n")

# Planet and color lists
my_planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
my_planets_colors = ["lightgrey", "darkorange", "royalblue", "crimson", "goldenrod", "khaki", "lightskyblue", "dodgerblue"]


# Plant radius
planet_radii = [20, 25, 28, 22, 35, 32, 30, 39]

# Draw planets if user selects 'y'
if other_planets.lower() == "y":
    tloc = 150  # Starting y-coordinate
    for i in range(len(my_planets)):
        planet = trtl.Turtle()
        planet.shape("star")  # Use circle for planets
        planet.fillcolor(my_planets_colors[i])  # Set color from list
        planet.penup()
        planet.goto(-150, tloc)  # Position planet
        planet.pendown()
        planet.begin_fill()
        planet.circle(20)  # Smaller radius for visibility
        planet.end_fill()
        tloc -= (planet_radii[i] * 2 + 10)  # Move down for next planet

# Keep the window open
screen.mainloop()