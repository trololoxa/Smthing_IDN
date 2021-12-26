from MainVersion.Buttons import SceneButton
from ursina import application, color, Button

scenes = []
LoadScene = []
SecondScene = []
CurrentScene = LoadScene
scenes.append(LoadScene)
scenes.append(SecondScene)


def init_scenes():
    ngb = SceneButton(
        text='New game',
        color=color.black,
        scale=(.25, .12, .25),
        next_scene=SecondScene,
        current_scene=CurrentScene,
        position=(-0.75, 0.43, 0))
    lgb = SceneButton(
        text='Load game',
        color=color.black,
        scale=(.25, .12, .25),
        next_scene=SecondScene,
        current_scene=CurrentScene,
        position=(-0.75, 0.305, 0))
    ext = Button(
        text='Exit',
        color=color.black,
        scale=(.25, .12, .25),
        position=(-0.75, 0.18, 0))
    ext.on_click = application.quit
    LoadScene.append(ngb)
    LoadScene.append(lgb)
    LoadScene.append(ext)

    b2 = Button(
        text='Nooo boi',
        color=color.green,
        scale=.25)
    b2.position = (-0.75, 0.35, 0)
    b2.on_click = application.quit
    b2.disable()
    SecondScene.append(b2)
