class DevError(BaseException):

    def __init__(self):
        self.info = 'This is a developer error. Please file an issue or see documentation if no more information is ' \
                    'provided'


class NotYetImplementedError(DevError, BaseException):

    def __init__(self):
        self.msg = 'This feature has not yet been implemented.'
        self.info = DevError().info
