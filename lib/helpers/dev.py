import os


def dev_complete(key_path=None):
    if key_path is None:
        key_path = str(os.getcwd() + '/dev.key')
    with open(key_path, 'w') as key_file:
        key_file.write('Mischief Managed!')
