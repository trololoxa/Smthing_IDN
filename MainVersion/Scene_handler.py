from MainVersion.Buttons import SceneButton
from ursina import application, color, Button

class Scene:
    def __init__(self, scene=None):
        if scene is None:
            scene = []
        self.scene = scene

    def disable_scene(self):
        for i in self.scene:
            i.disable()

    def enable_scene(self):
        for i in self.scene:
            i.enable()

    def on_click(self):
        self.current_scene.disable_scene()
        self.next_scene.enable_scene()


LoadScene = [Scene()]
MainScene = [Scene()]
CurrentScene = LoadScene

LoadScene[0] = Scene([
        SceneButton(
            text='New game',
            color=color.black,
            scale=(.25, .12, .25),
            next_scene=MainScene[0],
            current_scene=CurrentScene[0],
            position=(-0.75, 0.43, 0)),
        SceneButton(
            text='Load game',
            color=color.black,
            scale=(.25, .12, .25),
            next_scene=MainScene[0],
            current_scene=CurrentScene[0],
            position=(-0.75, 0.305, 0)),
        Button(
            text='Exit',
            color=color.black,
            scale=(.25, .12, .25),
            position=(-0.75, 0.18, 0),
            on_click=application.quit)
    ])
MainScene[0] = Scene([Button(
            text='Nooooo(((',
            color=color.black,
            scale=(.25, .12, .25),
            position=(-0.75, 0.18, 0),
            on_click=application.quit)])
MainScene[0].disable_scene()
CurrentScene = LoadScene

