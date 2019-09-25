#   a116_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl
import time

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  new_color = turtle_colors.pop() #get a color
  t.color(new_color) #assign the turtle a color
  my_turtles.append(t)

#  
start_x = t.xcor()
start_y = t.ycor()

#
count = 1
for t in my_turtles:
  t.penup()
  t.turtlesize(1 *count)
  t.pensize(1 *count)
  t.goto(start_x, start_y)
  t.pendown()
  t.right(45 *count)     
  t.forward(15 *count)
  time.sleep(1)
  count += 1

  #	
  start_x = t.xcor()
  start_y = t.ycor()

wn = trtl.Screen()
wn.mainloop()