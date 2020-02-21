#!/usr/bin/env python3

import argparse

def _mm(key_path):
    with open(key_path, 'w') as key_file:
        key_file.write('Mischief Managed!')



def compare_key(key_path):
    passphrase = 'I solemnly swear that I am up to no good.'
    with open(key_path) as keyfile:
        first_line = keyfile.readline().strip
        if first_line() == passphrase:
            from pyfiglet import Figlet
            banner = 'Dev-Mode'
            custom_fig = Figlet(font='epic')
            print(custom_fig.renderText(banner))
            print('Welcome developer, or curious user...')
            _mm(key_path)
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
    usage='python3 __main__.py',
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
            parser.add_argument('+dev', '+dev_mode',
                        action='store_true',
                        help='Super-Duper Dev Mode')


parser.add_argument('~p1', '~~player1_name',
                    required=False,
                    action='store',
                    default='Player One',
                    dest='p1_name',
                    help='Specify a name for player one from the command-line. One white-space is allowed in this '
                         'argument')

parser.add_argument('~p2', '~~player2_name',
                    required=False,
                    action='store',
                    default='Player Two',
                    dest='p2_name',
                    help='Specify a name for player two from the command-line. One white-space is allowed in this '
                         'argument')


args = parser.parse_args()


import pong

pong.__init__(args.p1_name, args.p2_name)
