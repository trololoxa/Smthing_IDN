from ursina import application, color, Button
from ursina.prefabs.dropdown_menu import DropdownMenu
from MainVersion.scene_thingies import *
import MainVersion.Save_load
from MainVersion.Save_load import load


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
def m2w():
    disableScene(MainScene)
    enableScene(WorkScene)


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
        text='wok',
        color=color.black,
        scale=(.25, .12, .25),
        position=(-0.75, 0.305, 0),
        on_click=ll2cf),
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
        position=(-0.75, 0.305, 0),
        on_click=ll2cf),
    Button(
        text='Eat',
        color=color.black,
        scale=(.25, .12, .25),
        position=(-0.75, 0.305, 0),
        on_click=ll2cf),
    Button(
        text='Exit',
        color=color.black,
        scale=(.25, .12, .25),
        position=(-0.75, 0.305, 0),
        on_click=ll2cf),
]
disableScene(MainScene)
WorkScene = [
    Button(
        text='wok1',
        color=color.black,
        scale=(.25, .12, .25),
        position=(-0.75, 0.305, 0),
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
        position=(-0.75, 0.305, 0),
        on_click=ll2cf),

]
disableScene(WorkScene)

