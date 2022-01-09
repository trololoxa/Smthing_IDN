from ursina import application, color, Button
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
    load(false)
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
ChooseFileScene = []
disableScene(ChooseFileScene)
MainScene = [Button(
            text='Nooooo(((',
            color=color.black,
            scale=(.25, .12, .25),
            position=(-0.75, 0.43, 0),
            on_click=application.quit)]
disableScene(MainScene)

