#TODO: Start transfer game to Ursina(or smthing idn)
from ursina import *
import random

rand_gen = random.Random()
texoffset = 0.0


def update():
    cube.rotation_y += rand_gen.random() * time.dt * 100 * 0
    cube.rotation_x += rand_gen.random() * time.dt * 100 * 0
    cube.rotation_z += rand_gen.random() * time.dt * 100 + 1

    if held_keys['r']:
        red = rand_gen.random() * 255
        green = rand_gen.random() * 255
        blue = rand_gen.random() * 255
        cube.color = color.rgb(red, green, blue)

    global texoffset
    texoffset += time.dt * 0.2
    setattr(cube, "texture_offset", (0, texoffset))

    if mouse.hovered_entity == cube and mouse.left == True:
        info.visible = True
    else:
        info.visible = False

def input(key):
    if key == 'space':
        red = rand_gen.random() * 255
        green = rand_gen.random() * 255
        blue = rand_gen.random() * 255
        cube.color = color.rgb(red, green, blue)


app = Ursina()

window.title = 'My Gay'
window.borderless = False
window.fullscreen = False
window.exit_button.visible = False
window.fps_counter.enabled = True

cubes = []
cube = Entity(model='cube', color=color.orange, scale=(6,6,0.1), texture="waterfall", collider="box")
cubes.append(cube)

Text.size = 0.05
Text.default_resolution = 1080 * Text.size
info = Text(text="A powerful waterfall roaring on the mountains")
info.x = -0.5
info.y = 0.4
info.background = True
info.visible = False

app.run()
