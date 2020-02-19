# Simple Pong in Python3
# By Tayjaybabee

import turtle
import os
from time import sleep
import pygame.mixer

win = turtle.Screen()
win.title('Pong by Inspyre')
win.bgcolor('black')
win.setup(width=800, height=600)
win.tracer(0)


# Scoreboard
#  =========
#
# Initialize with the scores at 0
p1_score = 0
p2_score = 0


# Player 1
# ========
player_1 = turtle.Turtle()
player_1.speed(0)
player_1.shape('square')
player_1.color('blue')
player_1.shapesize(stretch_wid=5, stretch_len=1)
player_1.penup()
player_1.goto(-350, 0)

# Player 2
player_2 = turtle.Turtle()
player_2.speed(0)
player_2.shape('square')
player_2.color('blue')
player_2.shapesize(stretch_wid=5, stretch_len=1)
player_2.penup()
player_2.goto(+350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0, 0)

## Move ball by two pixels to x and y every time
ball.dx = 0.08
ball.dy = 0.08

# Score writer
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 00 | Player 2: 00", align="center", font=('Uroob', 21, 'italic'))


# Logic
# ======

# Move left paddle up
def player_1_up():
    y = player_1.ycor()
    y += 20
    player_1.sety(y)


# Move left paddle down
def player_1_down():
    y = player_1.ycor()
    y -= 20
    player_1.sety(y)


# Move right paddle up
def player_2_up():
    y = player_2.ycor()
    y += 20
    player_2.sety(y)


# Move right paddle down
def player_2_down():
    y = player_2.ycor()
    y -= 20
    player_2.sety(y)


# Bind keyboard
win.listen()

# Call player_1_up when player-one presses "w"
win.onkeypress(player_1_up, 'w')

# Call player_1_down when player-one presses "s"
win.onkeypress(player_1_down, 's')


# Call player_2_up when player-two presses Up Arrow
win.onkeypress(player_2_up, 'Up')

# Call player_2_down when player-two presses down Arrow
win.onkeypress(player_2_down, 'Down')

# Main game-loop
started = False

pygame.mixer.init(frequency=480000, buffer=512,)
pygame.mixer.music.load('background_loop.wav')

while True:
    win.update()

    if not started:
        sleep(1)
        pen.goto(0,0)
        pen.clear()
        pen.write('Get Ready!', align='center', font=('Uroob', 40, 'bold'))
        os.system('aplay game_start.wav')
        pen.clear()
        pen.goto(0,260)
        pen.write("Player 1: 00 | Player 2: 00", align="center", font=('Uroob', 21, 'italic'))
        pygame.mixer.music.play()
        started = True



    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Collision
    # ================

    # Top border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("aplay top_bottom_hit.wav&")

    # Bottom border
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("aplay top_bottom_hit.wav&")

    # Right Goal
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        print("Player 1 Scored!")
        p1_score += 1  # Increment Player One's score
        pen.clear()
        os.system('aplay score.wav&')
        pen.goto(0, 0)
        pen.write('Player One Scored!', align='center', font=('Uroob', 40, 'bold'))
        sleep(2)
        pen.clear()
        pen.goto(0, 260)
        pen.write(f"Player 1: {p1_score} | Player 2: {p2_score}", align="center", font=('Uroob', 21, 'italic'))

    # Left goal
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        print("Player 2 Scored!")
        p2_score += 1  # Increment Player Two's score
        pen.clear()
        os.system('aplay score.wav&')
        pen.goto(0,0)
        pen.write('Player Two Scored!', align='center', font=('Uroob', 40, 'bold'))
        sleep(2)
        pen.clear()
        pen.goto(0, 260)
        pen.write(f"Player 1: {p1_score} | Player 2: {p2_score}", align="center", font=('Uroob', 21, 'italic'))


    # Paddle and Ball Collision
    # =========================

    # Player 1 Ball Collision
    if ball.xcor() < -340 and player_1.ycor() + 50 > ball.ycor() > player_1.ycor() - 50:
        os.system('aplay hit_paddle_1.wav&')
        ball.setx(-340)
        ball.dx *= -1


    # Player 2 Ball Collision
    if ball.xcor() > 340 and player_2.ycor() + 50 > ball.ycor() > player_2.ycor() - 50:
        os.system('aplay hit_paddle_2.wav&')
        ball.setx(340)
        ball.dx *= -1




