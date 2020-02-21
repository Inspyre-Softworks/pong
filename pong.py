# Simple Pong in Python3
# By Tayjaybabee

import turtle
import os
import time
import datetime
from time import sleep

import pygame

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
ball.dx = 5
ball.dy = 5

# Score writer
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 00 | {timer} | Player 2: 00", align="center", font=('Uroob', 21, 'italic'))


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


def write_score():
    pen.clear()
    pen.goto(0, 250)
    time_now = time.time()
    dif = time_now - time_start
    dif_time = str(datetime.timedelta(seconds=dif))
    dif_splt = dif_time.split(sep=':')
    timer = str(f'{dif_splt[1]}m {round(float(dif_splt[2]))}s')
    pen.write(f"Player 1: {p1_score} | {timer} | Player 2: {p2_score}", align="center", font=('Uroob', 21, 'italic'))


paused = False
paused_seconds = 0

while paused:
    paused_seconds += .5
    sleep(.5)


def _toggle_pause_():
    global paused
    if paused:
        paused = False
        bgmusic.music.unpause()
        write_score()
    else:
        paused = True
        bgmusic.music.pause()
        pen.clear()
        pen.goto(0, 0)
        pen.write('Paused', align='center', font=('Uroob', 40, 'bold'))


# Toggle paused
def pause_game(no_toggle=False):
    global paused
    if no_toggle == False:
        _toggle_pause_()


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

# Call pause_game when Escape key is pressed
win.onkeypress(pause_game, 'Escape')

# Main game-loop
started = False

bgmusic = pygame.mixer
bgmusic.init(frequency=48000)
bgmusic.music.load('background_loop.mp3')
sfx = pygame.mixer
sfx.init(frequency=44100)

sound_gamestart = sfx.Sound('game_start.wav')
sound_paddle1 = sfx.Sound('hit_paddle_1.wav')
sound_paddle2 = sfx.Sound('hit_paddle_2.wav')
sound_score = sfx.Sound('score.wav')
sound_topbottomhit = sfx.Sound('top_bottom_hit.wav')

time_start = time.time()

seconds_paused = 0
last_paused = False


def update_time():
    global time_start, paused, seconds_paused, last_paused
    while not paused:
        time_now = time.time()
        dif = time_now - time_start
        dif_time = str(datetime.timedelta(seconds=dif))
        dif_splt = dif_time.split(sep=':')
        timer = str(f'{dif_splt[1]}m {round(float(dif_splt[2]))}s')
        return timer


def move_ball():
    global p1_score, p2_score, win, ball, seconds_paused, time_start

    win.update()

    while paused:
        sleep(0.1)
        seconds_paused += .1
        print(seconds_paused)
        win.update()

    if seconds_paused >= .1:
        time_start += seconds_paused
        seconds_paused = 0
        write_score()


    write_score()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    # Border Collision
    # ================

    # Top border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        sound_topbottomhit.play()

    # Bottom border
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        sound_topbottomhit.play()

    # Right Goal
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        print("Player 1 Scored!")
        p1_score += 1  # Increment Player One's score
        pen.clear()
        sound_score.play()
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
        sound_score.play()
        pen.goto(0, 0)
        pen.write('Player Two Scored!', align='center', font=('Uroob', 40, 'bold'))
        sleep(2)
        pen.clear()
        pen.goto(0, 260)
        pen.write(f"Player 1: {p1_score} | Player 2: {p2_score}", align="center", font=('Uroob', 21, 'italic'))

    # Paddle and Ball Collision
    # =========================

    # Player 1 Ball Collision
    if ball.xcor() < -340 and player_1.ycor() + 50 > ball.ycor() > player_1.ycor() - 50:
        sound_paddle1.play()
        ball.setx(-340)
        ball.dx *= -1

    # Player 2 Ball Collision
    if ball.xcor() > 340 and player_2.ycor() + 50 > ball.ycor() > player_2.ycor() - 50:
        sound_paddle2.play()
        ball.setx(340)
        ball.dx *= -1

    win.ontimer(move_ball, 30)


move_ball()
turtle.mainloop()
