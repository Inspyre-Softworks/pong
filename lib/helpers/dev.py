import logging
from os import getcwd, path

logger_name = 'InsPyPong'

log = logging.getLogger('InsPyPong')


def _key_exists(key_path):
    from os import path

    l_log = logging.getLogger(f'{logger_name}._key_exists')
    l_log.debug(f'Checking to see if keyfile exists')
    if path.isfile(key_path):
        l_log.debug(f'Found a developer keyfile!')
        return True
    else:
        l_log.debug(f'Did not find a developer keyfile.')
        return False


def _phrase_matches(key_path):
    l_log = logging.getLogger(f'{logger_name}._phrase_matches')
    from lib.conf.misc import dev_phrase
    l_log.debug('Importing passphrase')
    passphrase = dev_phrase
    l_log.debug('Checking to see if passphrase matches imported passphrase')
    with open(key_path) as keyfile:
        first_line = keyfile.readline().strip
        if first_line() == '':
            l_log.warning('Found -nothing- in keyfile!')
        else:
            l_log.debug(f'Found "{first_line()}" in keyfile')

        if first_line() == passphrase:
            l_log.debug('We have a match')
            return True
        else:
            l_log.warning('Your access has been denied. Worry not, better than you have tried.')
            return False


def dev_complete(key_path):
    """

    Mark the dev keyfile indicating that you've finished with dev-mode.

    Note: Once you've done this you will have to re-submit the pass-phrase to the keyfile before running again. Doing so
    will not reactivate dev-mode for the current session.

    :param key_path: STRING - A string containing a path to the keyfile
    :return: None
    """

    l_log = logging.getLogger(f'{logger_name}.MaraudersMap')

    if key_path is None:
        key_path = str(getcwd() + '/dev.key')
    with open(key_path, 'w') as key_file:
        l_log.warning('Your mischief being managed, you\'ve shed your enhanced vantage.')
        key_file.write('Mischief Managed!')


def check(key_path=None):
    from lib.conf.paths import dev_key
    l_log = logging.getLogger(f'{logger_name}.check')
    if key_path is None:
        l_log.debug('Was not provided an alternate keypath, using default.')
        key_path = dev_key

    if _key_exists(key_path):
        if _phrase_matches(key_path):
            return True


def print_banner():
    """

    Print the developer-mode banner.

    :return:
    """
    from pyfiglet import Figlet

    banner = 'Dev-Mode'
    welcome = 'Welcome developer or curious user...'

    l_log = logging.getLogger(f'{logger_name}.print_banner')

    l_log.debug('Printing dev-mode banner')
    custom_fig = Figlet(font='epic')
    print(custom_fig.renderText(banner))
    l_log.debug('Banner printed.')
    l_log.debug('Printing welcome...')
    print(welcome)
    m_logger = logging.getLogger(f'{logger_name}.MaraudersMap')
    l_log.warning('You can now see what was once unseen, only troublemakers would be so keen.')


