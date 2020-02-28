# Simple Pong in Python3
# By Tayjaybabee

import turtle
import os
from time import sleep

import pygame

import argparse

parser = argparse.ArgumentParser(prog='InsPyPong',
                                 usage='pong ~p1=Taylor ~pc1=\'pink\' ~p2=Steve ~pc2=\'orange\' +v',
                                 description='Simple project for a simple (but complete) pong game',
                                 prefix_chars='~+',
                                 add_help=True)

parser.add_argument('~p1', '~~p1-name',
                    dest='P1_NAME',
                    action='store',
                    default='Player One',
                    help='Use this argument to tell the program what name Player One would like displayed in-game and '
                         'in scoreboards')

parser.add_argument('~p1c', '~~paddle1-color',
                    dest='PADDLE1_COLOR',
                    default='red',
                    action='store',
                    help='Use this argument to specify what color Player One\'s paddle will be')

parser.add_argument('~p2', '~~p2-name',
                    dest='P2_NAME',
                    default='Player Two',
                    action='store',
                    help='Use this argument to tell the program what name Player Two would like displayed in-game and '
                         'in scoreboards')

parser.add_argument('~p2c', '~~paddle2-color',
                    dest='PADDLE2_COLOR',
                    default='blue',
                    action='store',
                    help='Use this argument to specify what color Player Two\'s paddle will be')

parser.add_argument('+v', '~~verbose',
                    dest='verbose',
                    action='store_true',
                    help='Use this flag to tell the program to announce all there is to announce as it works.')

args = parser.parse_args()


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
player_1_name = args.P1_NAME
player_1 = turtle.Turtle()
player_1.speed(0)
player_1.shape('square')
player_1.color(args.PADDLE1_COLOR)
player_1.shapesize(stretch_wid=5, stretch_len=1)
player_1.penup()
player_1.goto(-350, 0)

# Player 2
player_2_name = args.P2_NAME
player_2 = turtle.Turtle()
player_2.speed(0)
player_2.shape('square')
player_2.color(args.PADDLE2_COLOR)
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
pen.write(f"{player_1_name}: 00 | {player_2_name}: 00", align="center", font=('Uroob', 21, 'italic'))


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


paused = False


def _toggle_pause_():
    global paused
    if paused:
        paused = False
        bgmusic.music.unpause()
    else:
        paused = True
        bgmusic.music.pause()


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

while True:
    win.update()

    while paused:
        sleep(0.1)
        win.update()

    if not started:
        sleep(1)
        pen.goto(0, 0)
        pen.clear()
        pen.write('Get Ready!', align='center', font=('Uroob', 40, 'bold'))
        sound_gamestart.play()
        sleep(sound_gamestart.get_length())
        pen.clear()
        pen.goto(0, 260)
        pen.write(f"{player_1_name}: 00 | {player_2_name}: 00", align="center", font=('Uroob', 21, 'italic'))
        bgmusic.music.play(-1)
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
        pen.write(f'{player_1_name} Scored!', align='center', font=('Uroob', 40, 'bold'))
        sleep(2)
        pen.clear()
        pen.goto(0, 260)
        pen.write(f"{player_1_name}: {p1_score} | {player_2_name}: {p2_score}", align="center", font=('Uroob', 21,
                                                                                                  'italic'))

    # Left goal
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        print("Player 2 Scored!")
        p2_score += 1  # Increment Player Two's score
        pen.clear()
        sound_score.play()
        pen.goto(0, 0)
        pen.write(f'{player_2_name} Scored!', align='center', font=('Uroob', 40, 'bold'))
        sleep(2)
        pen.clear()
        pen.goto(0, 260)
        pen.write(f"{player_1_name}: {p1_score} | {player_2_name}: {p2_score}", align="center", font=('Uroob', 21,
                                                                                                  'italic'))

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


