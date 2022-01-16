from ursina import application, color, Button
from ursina.prefabs.dropdown_menu import DropdownMenu, DropdownMenuButton

import Save_load
from MainVersion.Save_load import load


def disableScene(inputScene):
    for i in inputScene:
        i.disable()
def enableScene(inputScene):
    for i in inputScene:
        i.enable()
def ln2m():
    disableScene(LoadScene)
    load()
    enableScene(MainScene)
def ll2cf():
    disableScene(LoadScene)
    enableScene(ChooseFileScene)
def cf2m():
    disableScene(ChooseFileScene)
    enableScene(MainScene)


LoadScene = [
        Button(
            text='New game',
            color=color.black,
            scale=(.25, .12, .25),
            position=(-0.75, 0.43, 0),
            on_click=ln2m),
        Button(
            text='Load game',
            color=color.black,
            scale=(.25, .12, .25),
            position=(-0.75, 0.305, 0),
            on_click=ll2cf),
        Button(
            text='Exit',
            color=color.black,
            scale=(.25, .12, .25),
            position=(-0.75, 0.18, 0),
            on_click=application.quit)
    ]
class FileChooseButton(DropdownMenuButton):
    def __init__(self, text='', **kwargs):
        super().__init__(text, **kwargs)

    def on_click(self):
        load(False, self.text)
files = []
for i in range(len(Save_load.save_files)):
    files.append(FileChooseButton(Save_load.save_files[i]))
ChooseFileScene = [DropdownMenu('File', buttons=(
    files
    ))]
disableScene(ChooseFileScene)
MainScene = [Button(
            text='Nooooo(((',
            color=color.black,
            scale=(.25, .12, .25),
            position=(-0.75, 0.43, 0),
            on_click=application.quit)]
disableScene(MainScene)

