from ursina import *

app = Ursina()
a = InputField()
def update():
    print(a.text)
window.title = 'My Gay'
window.borderless = False
window.forced_aspect_ratio = (16, 9)
window.windowed_size = (1280, 720)
window.exit_button.visible = False
window.fps_counter.enabled = False
application.development_mode = False

app.run()
