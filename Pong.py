import turtle
import sys

#Create Window
win = turtle.Screen()

#Create Title 
win.title("Pong Pong Pong Pong Pong Pong Pong Pong Pong Pong Pong Pong Pong Pong Pong Pong Pong Pong ")

#Set Background Colour
win.bgcolor("black")

#Create 800 By 800 Pixel Screen
win.setup(width=800, height=600)

#Stops Window From Updating
win.tracer(0)

#Default Size Of A Square Is 20 By 20



################
### Paddle A ###
################



#Defines Paddle A As A Turtle
paddle_a = turtle.Turtle()

#Sets The Animation Speed
paddle_a.speed(0)

#Defines The Shape Of the Paddle
paddle_a.shape("square")

#Colours The Paddle
paddle_a.color("white")

#Stops The Turtle From Drawing Lines
paddle_a.penup()

#Changes Size Of Paddle
paddle_a.shapesize(stretch_wid=5, stretch_len=1)

#Move The Paddle To A Location
paddle_a.goto(-350, 0)



################
### Paddle B ###
################



#Defines Paddle B As A Turtle
paddle_b = turtle.Turtle()

#Sets The Animation Speed
paddle_b.speed(0)

#Defines The Shape Of the Paddle
paddle_b.shape("square")

#Colours The Paddle
paddle_b.color("white")

#Stops The Turtle From Drawing Lines
paddle_b.penup()

#Changes Size Of Paddle
paddle_b.shapesize(stretch_wid=5, stretch_len=1)

#Move The Paddle To A Location
paddle_b.goto(350, 0)



############
### Ball ###
############



#Defines Ball As A Turtle
ball = turtle.Turtle()

#Sets The Animation Speed
ball.speed(0)

#Defines The Shape Of The Ball
ball.shape("square")

#Colours The Ball
ball.color("white")

#Stops The Turtle From Drawing Lines
ball.penup()

#Move The Paddle To A Location
ball.goto(0, 0)

#Each Time Ball Moves It Moves 2 Tenths Of A Pixel
ball.dx = 0.3
ball.dy = 0.3



##############
### Points ###
##############

points1 = 0
points2 = 0

points = turtle.Turtle()
points.speed(0)
points.color("white")
points.penup()





#Function
def paddle_a_up():
    #Gets The Paddle's Y Position
    y = paddle_a.ycor()

    #Changes Y Value
    y += 20

    #Sets The Paddle's Location To The New Y Value
    paddle_a.sety(y)

def paddle_a_down():
    #Gets The Paddle's Y Position
    y = paddle_a.ycor()

    #Changes Y Value
    y -= 20

    #Sets The Paddle's Location To The New Y Value
    paddle_a.sety(y)

def paddle_b_up():
    #Gets The Paddle's Y Position
    y = paddle_b.ycor()

    #Changes Y Value
    y += 20

    #Sets The Paddle's Location To The New Y Value
    paddle_b.sety(y)

def paddle_b_down():
    #Gets The Paddle's Y Position
    y = paddle_b.ycor()

    #Changes Y Value
    y -= 20

    #Sets The Paddle's Location To The New Y Value
    paddle_b.sety(y)

def game_over():
    win.text("Game Over")
    sys.quit()





#Keyboard Bindings

#Listen For Keyboard Input
win.listen()

#When A Key Is Pressed Check Which Key And Move Paddle
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")







#Main Game Loop
while True:
    #Update Window
    win.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Comment

    #Border Check
    if ball.xcor() > 390:
        ball.setx(0)
        ball.sety(0)
        ball.dx *= -1
        points1 += 1
        points.goto(-50, 250)
        points.write(points1, False, "center", ("Arial", 36, "normal"))

    if ball.xcor() < -390:
        ball.setx(0)
        ball.sety(0)
        ball.dx *= -1
        points2 += 1
        points.goto(50, 250)
        points.write(points2, False, "center", ("Arial", 36, "normal"))

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if paddle_a.ycor() >= 250:
        paddle_a.sety(250)

    if paddle_a.ycor() <= -250:
        paddle_a.sety(-250)

    if paddle_b.ycor() >= 250:
        paddle_b.sety(250)

    if paddle_b.ycor() <= -250:
        paddle_b.sety(-250)

    if ball.xcor() < -340 and ball.xcor() > -360 and ball.ycor() > paddle_a.ycor() - 75 and ball.ycor() < paddle_a.ycor() + 75:
        ball.setx(-340)
        ball.dx *= -1

    if ball.xcor() < 360 and ball.xcor() > 340 and ball.ycor() > paddle_b.ycor() - 75 and ball.ycor() < paddle_b.ycor() + 75:
        ball.setx(340)
        ball.dx *= -1
