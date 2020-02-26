#!/usr/bin/env python3

player_list = []


class Register:
    from .errors import MaxPlayersError
    """
    A class to manage players for the Pong game.

    First you initialize the call into a variable, and then you use your new constructor to make a new player 
    object/class. This class will allow you to instanciate two player classes, P1 and P2. 

    P1 will be the player controlling the paddle on the left side of the screen 
    with the 'w' and 's' keys. (If you have capslock on it will 
    not work)

    P2 will be the player controlling the paddle on the right side of the screen
    with the 'Up' and 'Down' arrow keys.
    """

    def _register(self, name):
        _player = None

        if len(player_list) >= 2:
            from lib.pong.player.errors import MaxPlayersError
            raise MaxPlayersError(info='In this game there can only be two players', dev_tip=)

        if len(player_list) == 0:
            _player = P1(name)
            self.p1 = _player
        elif len(player_list) == 1:
            _player = P2(name)
            self.p2 = _player

        return _player

    def __init__(self):
        """
        Start a new instance of the Player class
        """
        self.p1 = None
        self.p2 = None

    def new_player(self, name):
        """
        A function that will allow one to register a new player
        :param name:
        :return:
        """
        from .errors import MaxPlayersError

        try:
            self._register(name)
        except MaxPlayersError() as e:


        self._register(name)

        player_list.append(name)


class P1:

    def __init__(self, name):
        import turtle
        super().__init__()
        self.name = name
        self.paddle = turtle.Turtle()
        self.paddle.speed(0)
        self.paddle.shape('square')
        self.paddle.color('blue')
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(-350, 0)


    # Move left paddle up
    def up(self):
        y = self.paddle.ycor()
        y += 20
        self.paddle.sety(y)


# Move left paddle down
def player_1_down():
    y = player_1.ycor()
    y -= 20
    player_1.sety(y)


class P2:

    def __init__(self, name):
        super().__init__()
        self.name = name


