from MainVersion.ChangeScene import *
from ursina import Button, application, color


def init_scenes():
    b1 = Button(text='Yeaa boi', color=color.black, scale=(.25, .12, .25))
    b1.position = (-0.75, 0.43, 0)
    b1.on_click = load2game
    LoadScene.append(b1)

    b2 = Button(text='Nooo boi', color=color.green, scale=.25)
    b2.position = (-0.75, 0.35, 0)
    b2.on_click = application.quit
    b2.disable()
    SecondScene.append(b2)
