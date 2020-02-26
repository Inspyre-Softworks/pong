import PySimpleGUIQt as qt

class InsPyPongInstaller:

    def __init__(self, destination_dir=None):
        import platform
        if destination_dir is None:
            if platform.uname().system == 'Windows':
                print('You are on Windows!')
                self.destination = 'C:/Program\ Files/Inspyre\ Softworks/insPyPong'
                qt.PopupGetFolder('Is this where you\'d like to install insPyPong from Inspyre Softworks?',
                                  initial_folder=self.destination)

            if platform.uname().system == 'Linux':
                print('You are on Linux!')

InsPyPongInstaller()
