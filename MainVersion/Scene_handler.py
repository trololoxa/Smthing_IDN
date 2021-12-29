from MainVersion.Buttons import SceneButton
from ursina import application, color, Button

class Scene:
    def __init__(self, scene):
        self.scene = scene

    def disable_scene(self):
        for i in self.scene:
            i.disable()

    def enable_scene(self):
        for i in self.scene:
            i.enable()
LoadScene = []
MainScene = []
CurrentScene = LoadScene

LoadScene = Scene([
        SceneButton(
            text='New game',
            color=color.black,
            scale=(.25, .12, .25),
            next_scene=MainScene,
            current_scene=CurrentScene,
            position=(-0.75, 0.43, 0)),
        SceneButton(
            text='Load game',
            color=color.black,
            scale=(.25, .12, .25),
            next_scene=MainScene,
            current_scene=CurrentScene,
            position=(-0.75, 0.305, 0)),
        Button(
            text='Exit',
            color=color.black,
            scale=(.25, .12, .25),
            position=(-0.75, 0.18, 0),
            on_click=application.quit)
    ])
MainScene = Scene([Button(
            text='Nooooo(((',
            color=color.black,
            scale=(.25, .12, .25),
            position=(-0.75, 0.18, 0),
            on_click=application.quit)])
MainScene.disable_scene()
