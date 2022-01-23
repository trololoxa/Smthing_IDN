from ursina import application, color, Button, Text
from ursina.prefabs.dropdown_menu import DropdownMenu, DropdownMenuButton
from MainVersion.scene_thingies import *
import MainVersion.Save_load
from MainVersion.Save_load import load, save

a=0
def ln2m():
    disableScene(LoadScene)
    load()
    enableScene(MainScene)
    enableScene(MainInfo)
def ll2cf():
    disableScene(LoadScene)
    enableScene(ChooseFileScene)
def cf2m():
    disableScene(ChooseFileScene)
    enableScene(MainScene)
    enableScene(MainInfo)
def m2w():
    disableScene(MainScene)
    enableScene(WorkScene)
def w2m():
    disableScene(WorkScene)
    enableScene(MainScene)
def m2l():
    disableScene(MainScene)
    disableScene(MainInfo)
    save(player.return_save_data())
    enableScene(LoadScene)
def printinfo():
    global a
    a+=1

class FileChooseButton(DropdownMenuButton):
    def __init__(self, text='', **kwargs):
        super().__init__(text, **kwargs)

    def on_click(self):
        load(False, self.text)
        cf2m()

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
files = []
for i in range(len(MainVersion.Save_load.save_files)):
    files.append(FileChooseButton(MainVersion.Save_load.save_files[i]))
ChooseFileScene = [
    DropdownMenu('File', buttons=files)
]
disableScene(ChooseFileScene)
MainScene = [
    Button(
        text='the wok',
        color=color.black,
        scale=(.25, .12, .25),
        position=(-0.75, 0.43, 0),
        on_click=m2w),
    Button(
        text='Upgrade PC',
        color=color.black,
        scale=(.25, .12, .25),
        position=(-0.75, 0.305, 0),
        on_click=ll2cf),
    Button(
        text='Sleep',
        color=color.black,
        scale=(.25, .12, .25),
        position=(-0.75, 0.18, 0),
        on_click=ll2cf),
    Button(
        text='Eat',
        color=color.black,
        scale=(.25, .12, .25),
        position=(-0.75, 0.055, 0),
        on_click=ll2cf),
    Button(
        text='Exit',
        color=color.black,
        scale=(.25, .12, .25),
        position=(-0.75, -0.07, 0),
        on_click=m2l),
]
MainInfo = [
    Text(
        text=str(a),
        color=color.black,
        scale=(1, 1, 1),
        position=(-0.5, 0.43, 0),
        on_click=ln2m)
]
disableScene(MainInfo)
disableScene(MainScene)
WorkScene = [
    Button(
        text='wok1',
        color=color.black,
        scale=(.25, .12, .25),
        position=(-0.75, 0.43, 0),
        on_click=ll2cf),
    Button(
        text='wok2',
        color=color.black,
        scale=(.25, .12, .25),
        position=(-0.75, 0.305, 0),
        on_click=ll2cf),
    Button(
        text='exit',
        color=color.black,
        scale=(.25, .12, .25),
        position=(-0.75, 0.18, 0),
        on_click=w2m),

]
disableScene(WorkScene)

