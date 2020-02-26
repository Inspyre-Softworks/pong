#!/usr/bin/env python3

import argparse

figlet_shown = False


def _mm(key_path):
    with open(key_path, 'w') as key_file:
        key_file.write('Mischief Managed!')


def compare_key(key_path):
    global figlet_shown
    passphrase = 'I solemnly swear that I am up to no good.'
    with open(key_path) as keyfile:
        first_line = keyfile.readline().strip
        if first_line() == passphrase:
            from pyfiglet import Figlet

            banner = 'Dev-Mode'
            if not figlet_shown:
                custom_fig = Figlet(font='epic')
                print(custom_fig.renderText(banner))
                print('Welcome developer, or curious user...')
                figlet_shown = True
            return True

    return False


def check_dev_key():
    from os import path, getcwd

    print(getcwd())
    print(str(getcwd() + '/dev.key'))
    if path.isfile(str(getcwd() + '/dev.key')):
        print('Found dev.key file')
        return True
    return False


parser = argparse.ArgumentParser(
    prog='Pong by Inspyre Softworks',
    usage='python3 __main__.py ~p1=<P1 NAME> ~p2c=<COLOR NAME OR HEX STRING> ~p2=<P2 NAME> ~p2c=<COLOR NAME OR HEX '
          'STRING>',
    description='Pong (by Inspyre Softworks) is just as it seems; our version of the Atari hit; Pong',
    epilog='Enjoy your game session',
    add_help=True,
    allow_abbrev=True,
    prefix_chars='~+'
    )

if check_dev_key():
    import os

    keypath = str(os.getcwd() + '/dev.key')
    if os.path.isfile(keypath):
        if compare_key(keypath):
            parser.add_argument('+dev', '+dev-mode',
                                action='store_true',
                                help='Super-Duper Dev Mode',
                                dest='dev_mode')

# Assign arguments that will set attributes for player 1
parser.add_argument(
    '~p1', '~~player1-name',
    required=False,
    action='store',
    default='Player One',
    dest='p1',
    help='Specify a name for player one from the command-line. One white-space is allowed in this '
         'argument'
    )

parser.add_argument(
    '~p1c', '~~player1-paddle-color',
    required=False,
    action='store',
    default='red',
    dest='p1_paddle_color',
    help='Designate the color you\'d like the Player One paddle to be',
    )

# Asssign arguments that will set attributes for player 2
parser.add_argument(
    '~p2', '~~player2-name',
    required=False,
    action='store',
    default='Player Two',
    dest='p2',
    help='Specify a name for player two from the command-line. One white-space is allowed in this '
         'argument'
    )

parser.add_argument(
    '~p2c', '~~player2-paddle-color',
    required=False,
    action='store',
    default='white',
    dest='p2_paddle_color',
    help='Designate the color you\'d like the Player Two paddle to be',
    )

# ToDo:
#     Assign arguments that will set attributes for the Ball
#     Assign arguments that will set attributes for the playing field/screen
#     Assign arguments that will redirect logging output (maybe)

args = parser.parse_args()
from lib.helpers.logger import start

log = start('InsPyPong')
log.debug('Logger started')
log.debug(f'My runtime configuration is: {args}')

if args.p1 == 'Player One' or args.p2 == 'Player Two':
    from lib.pong.gui.start_screen import StartScreen

    dev_mode = False

    if check_dev_key():
        import os

        keypath = str(os.getcwd() + '/dev.key')
        if os.path.isfile(keypath):
            if compare_key(keypath):
                if args.dev_mode:
                    dev_mode = True

    StartScreen(args.p1, args.p2, dev_mode=dev_mode)
else:
    import old_pong
