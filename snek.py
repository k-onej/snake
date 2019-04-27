from turtle import *
import time
screen_width, screen_height =900, 900
screen = Screen()
screen.setup(screen_width, screen_height)

#Border
# Turtle 1 Creation 
t0 = Turtle()
t0.hideturtle()
t0.speed(0)
t0.pensize(5)
t0.penup()
t0.goto(-screen_width / 2, - screen_height/2)
t0.pendown()
for i in range(4):
  t0.forward(screen_width)
  t0.left(90)



#orientation of the turtle (standard mode)
#   0 - East
# 90 - North
# 180 - West
# 270 - South
t1 = Turtle()

def red_up():
  t1.setheading(90)
  t1.fd(16)

def red_down():
  t1.setheading(270)
  t1.fd(16)

def red_left():
  t1.setheading(180)
  t1.fd(16)

def red_right():
  t1.setheading(0)
  t1.fd(16)


screen.onkey(red_down, 'Down')

screen.onkey(red_up, 'Up')

screen.onkey(red_right, 'Right')

screen.onkey(red_left, 'Left')



# Turtle 1 Creation 
t1.shape('square')
t1.color('green')
t1.penup()
t1.speed(0)




Screen().listen()
Screen().mainloop()






