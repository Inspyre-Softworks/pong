import PySimpleGUI as qt

layout = [
    [qt.Text('This is a text field'), qt.InputText('')],
    [qt.Button('OK')]
    ]

window = qt.Window('Test Window', layout=layout)

while True:
    event, values = window.read(timeout=100)
    
