#TODO: Start transfer game to Ursina(or smthing idn)
from ursina import *
import MainVersion.Scene_handler

app = Ursina()

window.title = 'My Gay'
window.borderless = False
window.forced_aspect_ratio = (16, 9)
window.windowed_size = (1280, 720)
window.exit_button.visible = False
window.fps_counter.enabled = False
application.development_mode = False

init_scenes()

app.run()
