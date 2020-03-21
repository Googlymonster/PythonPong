import turtle
import os

wn = turtle.Screen()
wn.title("Pong by @Googlymonster")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
scoreA = 0
scoreB = 0


# Paddle A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("white")
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.penup()
paddleA.goto(-350, 0)

# Paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.penup()
paddleB.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center",
          font=("Courier", 24, "normal"))

# Functions


def paddleA_up():
    y = paddleA.ycor()
    y += 20
    paddleA.sety(y)


def paddleA_down():
    y = paddleA.ycor()
    y -= 20
    paddleA.sety(y)


def paddleB_up():
    y = paddleB.ycor()
    y += 20
    paddleB.sety(y)


def paddleB_down():
    y = paddleB.ycor()
    y -= 20
    paddleB.sety(y)


# Keyboard binding
wn.listen()
wn.onkeypress(paddleA_up, "w")
wn.onkeypress(paddleA_down, "s")
wn.onkeypress(paddleB_up, "Up")
wn.onkeypress(paddleB_down, "Down")


# Main gamin loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreA += 1
        pen.clear()
        pen.write(f"Player A: {scoreA}  Player B: {scoreB}",
                  align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreB += 1
        pen.clear()
        pen.write(f"Player A: {scoreA}  Player B: {scoreB}",
                  align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddleB.ycor() + 50 and ball.ycor() > paddleB.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
    elif (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddleA.ycor() + 50 and ball.ycor() > paddleA.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
