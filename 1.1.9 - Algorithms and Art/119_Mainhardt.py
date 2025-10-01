import turtle as trtl

screen = trtl.Screen()
screen.bgcolor("black") # Set the background color to black



#custom defintion
trtl.addshape("star", ((0, 3), (2, 0), (4,-1), (2,-2), (3,-4), (1,-3), (-1,-3), (-3,-4), (-2,-2), (-4, -1), (-2, 0)))


#user texts
other_planets = trtl.textinput("Planets", "Do you want to see the planets? y/n")
if other_planets == "y":



 
#list
 my_planets = ["Mercury", "Venus", "Earth", "Mars", "Jupter", "Saturn", "Uranus", "Neptune"] #planets list
 my_planets_colors = ["grey", "orange", "blue", "darkred", "yellow", "gold", "cyan", "dodgerblue"]

#iteration

tloc = 10
for planets in my_planets:

 planets = trtl.Turtle()
 planets.circle(90)
 planets.fillcolor(my_planets_colors)
 planets.penup()
 planets.goto(-10, tloc)
 planets.setheading(0)





wn = trtl.Screen()
wn.mainloop()