class PlayerError(Exception):
    pass


class MaxPlayersError(PlayerError):

    def __init__(self, info=None, dev_tip=None):
        msg = 'Max ammount of players reached. Not registering anymore.'

        if info is None:
            self.info = msg

        if dev_tip is None:
            self.dev_tip = 'Nope'

        self.msg = msg


class InsufficientPlayerCountError(PlayerError):

    def __init__(self):
        pass
