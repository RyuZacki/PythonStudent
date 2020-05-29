
import turtle

win = turtle.Screen()
win.title("My paint")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# racket
racket_a = turtle.Turtle()
racket_a.speed(0)
racket_a.shape('square')
racket_a.color('blue')
racket_a.shapesize(stretch_len=1, stretch_wid=5)
racket_a.penup()
racket_a.goto(-350, 0)

racket_b = turtle.Turtle()
racket_b.speed(0)
racket_b.shape('square')
racket_b.color('yellow')
racket_b.shapesize(stretch_len=1, stretch_wid=5)
racket_b.penup()
racket_b.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 || Player B: 0", align='center', font=('Verdana', 22, 'normal'))

score_a = 0
score_b = 0

# Functions
def racket_a_up():
    y = racket_a.ycor()
    y += 20
    racket_a.sety(y)

def racket_a_down():
    y = racket_a.ycor()
    y -= 20
    racket_a.sety(y)

def racket_b_up():
    y = racket_b.ycor()
    y += 20
    racket_b.sety(y)

def racket_b_down():
    y = racket_b.ycor()
    y -= 20
    racket_b.sety(y)

# keyboard
win.listen()
win.onkeypress(racket_a_up, "w")
win.onkeypress(racket_a_down, "s")
win.onkeypress(racket_b_up, "Up")
win.onkeypress(racket_b_down, "Down")


while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} || Player B: {}".format(score_a, score_b), align='center', font=('Verdana', 22, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} || Player B: {}".format(score_a, score_b), align='center', font=('Verdana', 22, 'normal'))

    if ball.xcor() > 340 and ball.ycor() < racket_b.ycor() + 50 and ball.ycor() > racket_b.ycor() - 50:
        ball.dx *= -1

    if ball.xcor() < -340 and ball.ycor() < racket_a.ycor() + 50 and ball.ycor() > racket_a.ycor() - 50:
        ball.dx *= -1