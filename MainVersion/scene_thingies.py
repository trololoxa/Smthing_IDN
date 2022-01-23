from ursina.prefabs.dropdown_menu import DropdownMenuButton
from ursina import Button
from MainVersion.Save_load import load

def disableScene(inputScene):
    for i in inputScene:
        i.disable()
def enableScene(inputScene):
    for i in inputScene:
        i.enable()

class FileChooseButton(DropdownMenuButton):
    def __init__(self, text='', **kwargs):
        super().__init__(text, **kwargs)

    def on_click(self):
        load(False, self.text)


class WorkButton(Button):
    def __init__(self, text, player, **kwargs):
        super().__init__(text, **kwargs)
        self.player = player

    def on_click(self):
        worknum = self._on_click
        self.player.work(worknum)

