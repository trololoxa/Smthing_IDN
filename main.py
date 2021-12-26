#TODO: Start transfer game to Ursina(or smthing idn)
#Ursina
from ursina import *
import random
from MainVersion.Scenes import init_scenes

rand_gen = random.Random()


def update():
    pass


def input(key):
    pass


app = Ursina()

window.title = 'My Gay'
window.borderless = False
window.forced_aspect_ratio = (16,9)
window.windowed_size = (1280, 720)
window.exit_button.visible = False
window.fps_counter.enabled = False
application.development_mode = False

init_scenes()
"""
class Option(Button):
  def __init__(self):
    super().__init__(
      model = 'circle',
      texture = 'brick',
      color = color.blue,
      scale = 0.3)

  def on_click():
    doSomething()
"""
"""
wp = WindowPanel(
    title='Custom Window',
    content=(
        Text('Name:'),
        InputField(name='name_field'),
        Button(text='Submit', color=color.azure),
        Slider(),
        Slider(),
        ),
        popup=True,
        enabled=False
    )

def input(key):
    if key == 'space':
        wp.enabled = True
"""

app.run()
"""from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.gui.DirectGui import *


class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.taskMgr.add(self.checkBtnTask, "CheckBtnTask")

    def checkBtnTask(self, task):
        print(b.state)


b = DirectButton(text=("OK", "click!", "rolling over", "disabled"))
b.setScale(0.1)
b.commandFunc()

app = MyApp()
app.run()"""