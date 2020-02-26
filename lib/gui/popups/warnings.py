import PySimpleGUIQt as qt


def not_yet_implemented():
    from lib.conf.txt import font
    qt.PopupError('This feature is not yet implemented',
                  title='Developer Error',
                  font=(font, 12),
                  keep_on_top=True)
