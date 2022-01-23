from ursina import Button
from MainVersion.Save_load import player

def disableScene(inputScene):
    for i in inputScene:
        i.disable()
def enableScene(inputScene):
    for i in inputScene:
        i.enable()


class WorkButton(Button):
    def __init__(self, text, **kwargs):
        super().__init__(text, **kwargs)

    def on_click(self):
        worknum = self._on_click
        player.work(worknum)

