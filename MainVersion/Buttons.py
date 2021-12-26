from ursina import Button


class SceneButton(Button):
    def __init__(self, text='', next_scene=None, current_scene=None, **kwargs):
        super().__init__(text, **kwargs)
        self.current_scene = current_scene
        self.next_scene = next_scene

    def on_click(self):
        for i in self.current_scene:
            i.disable()
        for i in self.next_scene:
            i.enable()
