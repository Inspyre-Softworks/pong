
import PySimpleGUIQt as qt



class StartScreen:
    """

    The class that will act as the main start/options screen for insPyPong

    """

    def _p1_frame(self):
        layout = [
            [
                qt.Text('Name:', background_color='black'),
                qt.InputText(self.p1_name, key='P1_NAME',
                             background_color='black',
                             text_color='white',
                             focus=True)
             ],
            [
                qt.Text('Paddle Color:', background_color='black'),
                qt.InputText(self.paddle1_color,
                             key='P1_PADDLE_COLOR_INPUT',
                             visible=self.dev_mode,
                             enable_events=True),
                qt.ColorChooserButton('Select',
                                      key='P1_PADDLE_COLOR',
                                      button_color=('white', self.paddle1_color),
                                      target=(qt.ThisRow, -1))
             ]
        ]
        return layout

    def _p2_frame(self):
        layout = [
            [
                qt.Text('Name:', background_color='black'),
                qt.InputText(self.p2_name, key='P2_NAME',
                             background_color='black',
                             text_color='white')
            ],
            [
                qt.Text('Paddle Color:', background_color='black'),
                qt.InputText('', key='P2_PADDLE_COLOR_INPUT', visible=self.dev_mode, enable_events=True),
                qt.ColorChooserButton('Select',
                                      key='P2_PADDLE_COLOR',
                                      button_color=('white', self.paddle2_color),
                                      target=(qt.ThisRow, -1))
            ]
        ]
        return layout

    def _button_frame(self):
        layout = [
            [
                qt.Button('Play', bind_return_key=True, key='PLAY_BUTTON'),
                qt.Button('Cancel', key='CANCEL_BUTTON')
             ],
            [
                qt.Button('Debugger', key='DEBUG_BUTTON', visible=self.dev_mode),
                qt.Button('Mischief Managed!', visible=self.dev_mode, key='MISCHIEF_MANAGED')
            ]
        ]

        return layout

    def _layout(self):
        layout = [
            [qt.Frame('Player One:', self._p1_frame(), background_color='black')],
            [qt.Frame('Player Two:', self._p2_frame(), background_color='black')],
            [qt.Frame('', self._button_frame())]
        ]
        return layout

    def __init__(self, p1_name, p2_name, dev_mode=False):
        """

        Create a new instance of StartScreen

        :param p1_name:
        :param p2_name:
        :param dev_mode:
        """
        import logging

        self.log = logging.getLogger(f'InsPyPong.StartScreen')
        log = self.log

        # Make dev_mode an attribute of the StartScreen class
        self.dev_mode = dev_mode
        log.debug(f'Running in developer mode: {dev_mode}')

        # Set default paddle color values
        self.p1_name = p1_name
        self.paddle1_color = '#ff0000'

        self.p2_name = p2_name
        self.paddle2_color = 'blue'

        layout = self._layout()

        window = qt.Window('Pong Start Screen',
                           layout=layout,
                           resizable=True,
                           background_color='black',
                           size=(300, 300),
                           font=('Urood', 12)
                           )

        dev_fields = ['P1_PADDLE_COLOR_INPUT', 'P2_PADDLE_COLOR_INPUT', 'DEBUG_BUTTON', 'MISCHIEF_MANAGED']

        while True:
            event, values = window.Read()

            # Our invisible InputText element changes, so we change the color of the button and the associated
            # StartScreen attribute to the chosen color
            if event == 'P1_PADDLE_COLOR_INPUT':
                self.paddle1_color = values['P1_PADDLE_COLOR_INPUT']
                log.debug('A new color was picked for paddle 1')
                log.debug('Changing color of paddle 1')
                window['P1_PADDLE_COLOR'].update(button_color=('white', self.paddle1_color))
                log.debug(f'The color chooser button is now {self.paddle1_color}')

            # Same as above block, but for player 2
            if event == 'P2_PADDLE_COLOR_INPUT':
                self.paddle2_color = values['P2_PADDLE_COLOR_INPUT']
                window['P2_PADDLE_COLOR'].update(button_color=('white', self.paddle2_color))

            if event == 'PLAY_BUTTON':
                import subprocess
                import sys
                log.debug('User indicated a desire to start the game.')
                log.info('Starting game!')
                log.debug('Concatenating start command for game')

                cmd = [sys.executable, 'old_pong.py', f'~p1={values["P1_NAME"]}', f'~p1c={self.paddle1_color}',
                       f'~p2={values["P2_NAME"]}', f'~p2c={self.paddle2_color}']

                game = subprocess.Popen(cmd)
                game.communicate()


            # If the Cancel button or X button are clicked, the window closes and the program exits
            if event is None or event == 'CANCEL_BUTTON':
                window.close()
                exit()

            if event == qt.TIMEOUT_KEY:
                window.read()
                continue

            # If the Debugger button is pressed then an imwatchingyou debugger window shall appear

            if event == 'DEBUG_BUTTON':
                try:
                    from lib.helpers.errors.dev import NotYetImplementedError
                    raise NotYetImplementedError
                except NotYetImplementedError as e:
                    from lib.gui.popups.warnings import not_yet_implemented
                    print(e.msg)
                    print(e.info)
                    not_yet_implemented()
            #     imwatchingyou.show_debugger_window(location=(0, 0))


            # If the user presses the Mischief Managed button, the dev.key file will be nullified
            if event == 'MISCHIEF_MANAGED':
                from lib.helpers.dev import dev_complete
                from lib.conf.paths import dev_key

                confirm = qt.PopupYesNo('Are you sure you want to disable dev-mode?',
                                        title='Disable Dev-Mode Confirm',
                                        background_color='black',
                                        text_color='white',
                                        keep_on_top=True)

                if confirm.lower() == 'yes':
                    dev_complete(dev_key)
                    for field in dev_fields:
                        window[field].update(visible=False)
                        window.refresh()

