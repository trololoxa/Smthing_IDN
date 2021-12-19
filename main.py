#TODO: Start transfer game to Ursina(or smthing idn)
from ursina import *
import random

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
window.fps_counter.enabled = True

b = Button(text='Yeaa boi', color=color.black, scale=.25)
b.position = (-0.75,0.35,0)
b.on_click = application.quit

app.run()
