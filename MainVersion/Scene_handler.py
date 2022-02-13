from ursina import application, color, Button, Text, InputField
from ursina.prefabs.dropdown_menu import DropdownMenu, DropdownMenuButton

import Save_load
from MainVersion.scene_thingies import *
import MainVersion.Save_load
from MainVersion.Save_load import load, save

def ln2nf():
    disableScene(LoadScene)
    enableScene(SaveNameScene)
def nf2m():
    Save_load.player.file_name = SaveNameScene[0].text
    disableScene(SaveNameScene)
    enableScene(MainScene)
    updateinfo()
    enableScene(MainInfo)
def ll2cf():
    disableScene(LoadScene)
    enableScene(ChooseFileScene)
def cf2m():
    disableScene(ChooseFileScene)
    enableScene(MainScene)
    updateinfo()
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
    save(Save_load.player.return_save_data())
    enableScene(LoadScene)
def wok1():
    Save_load.player.work(1)
    updateinfo()
def wok2():
    Save_load.player.work(2)
    updateinfo()
def wok3():
    Save_load.player.work(3)
    updateinfo()
def upgrade_pc():
    Save_load.player.upgrade_pc()
    updateinfo()
def eat():
    Save_load.player.eat()
    updateinfo()
def sleep():
    Save_load.player.sleep()
    updateinfo()
def updateinfo():
    info = Save_load.player.return_save_data()
    MainInfo[0].text = 'Money = ' + str(info[1])
    MainInfo[1].text = 'PC = ' + str(Save_load.player.PC.tiers[info[2]])
    MainInfo[2].text = 'Hunger = ' + str(info[3])
    MainInfo[3].text = 'Days = ' + str(info[4]['days'])
    MainInfo[4].text = 'Hours = ' + str(info[4]['hours'])
    MainInfo[5].text = 'Cheerfulness = ' + str(info[5])

class FileChooseButton(DropdownMenuButton):
    def __init__(self, text='', **kwargs):
        super().__init__(text, **kwargs)

    def on_click(self):
        load(False, self.text)
        print(self.text)
        print(Save_load.player.return_save_data())
        cf2m()

LoadScene = [
    Button(
        text='New game',
        color=color.black,
        scale=(.25, .12, .25),
        position=(-0.75, 0.43, 0),
        on_click=ln2nf),
    Image(
        'Selfie\\Чёрнорабочий.jpg',
        scale=(.5, .24, .5),
        position=(-0.37, 0.3675, 0)),
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
        on_click=application.quit),
    Image(
        'Selfie\\ГЕЙ ПАТИ.jpg',
        scale=(.5, .12, .5),
        position=(-0.37, 0.18, 0)),
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
        on_click=upgrade_pc),
    Button(
        text='Sleep',
        color=color.black,
        scale=(.25, .12, .25),
        position=(-0.75, 0.18, 0),
        on_click=sleep),
    Button(
        text='Eat',
        color=color.black,
        scale=(.25, .12, .25),
        position=(-0.75, 0.055, 0),
        on_click=eat),
    Button(
        text='Exit',
        color=color.black,
        scale=(.25, .12, .25),
        position=(-0.75, -0.07, 0),
        on_click=m2l),
]
MainInfo = [
    Text(
        text=str(0),
        color=color.black,
        scale=(1, 1, 1),
        position=(0, 0.43, 0)),
    Text(
        text=str(0),
        color=color.black,
        scale=(1, 1, 1),
        position=(0, 0.305, 0)),
    Text(
        text=str(0),
        color=color.black,
        scale=(1, 1, 1),
        position=(0, 0.18, 0)),
    Text(
        text=str(0),
        color=color.black,
        scale=(1, 1, 1),
        position=(0, 0.055, 0)),
    Text(
        text=str(0),
        color=color.black,
        scale=(1, 1, 1),
        position=(0, -0.07, 0)),
    Text(
        text=str(0),
        color=color.black,
        scale=(1, 1, 1),
        position=(0, -0.195, 0)),

]
disableScene(MainInfo)
disableScene(MainScene)
WorkScene = [
    Button(
        text='PC Freelance',
        color=color.black,
        scale=(.25, .12, .25),
        position=(-0.75, 0.43, 0),
        on_click=wok1),
    Button(
        text='Street cleaner',
        color=color.black,
        scale=(.25, .12, .25),
        position=(-0.75, 0.305, 0),
        on_click=wok2),
    Button(
        text='Car cleaner',
        color=color.black,
        scale=(.25, .12, .25),
        position=(-0.75, 0.18, 0),
        on_click=wok3),
    Button(
        text='exit',
        color=color.black,
        scale=(.25, .12, .25),
        position=(-0.75, 0.055, 0),
        on_click=w2m)
]
disableScene(WorkScene)
SaveNameScene = [
    InputField(),
    Button(
        text='Load',
        color=color.black,
        scale=(.25, .05, .25),
        position=(0.379, 0, 0),
        on_click=nf2m)
]
disableScene(SaveNameScene)

