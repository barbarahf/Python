# pong game

import turtle

wn = turtle.Screen()
wn.title("Juego pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)

wn.tracer(0)  # actualizar manualmente

# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)  # Animacion
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("white")
paddle_a.penup()  # lines
paddle_a.goto(-350, 0)
# B
paddle_b = turtle.Turtle()
paddle_b.speed(0)  # Animacion
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("white")
paddle_b.penup()  # lines
paddle_b.goto(350, 0)

# Pelota
pelota = turtle.Turtle()
pelota.speed(0)  # Animacion
pelota.shape("square")
pelota.color("white")
pelota.penup()  # lines
pelota.goto(0, 0)

pelota.dx = 0.1
pelota.dy = -0.1


# Funciones
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


# B
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Input del teclado
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
# game loop

while True:
    wn.update()
    # mover pelota
    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)
    # top bottom
    if pelota.ycor() > 290:
        pelota.sety(290)
        pelota.dy *= -1
    if pelota.ycor() < -290:
        pelota.sety(-290)
        pelota.dy *= -1
    # left right
    if pelota.xcor() > 390:
        pelota.goto(0, 0)
        pelota.dx *= -1
    if pelota.xcor() < -390:
        pelota.goto(0, 0)
        pelota.dx *= -1