from ursina import *

app = Ursina()


class image(Entity):
    def __init__(self, texture, **kwargs):
        super().__init__(
            parent=camera.ui,
            model='quad',
            texture=texture,
            **kwargs)


image(
    'Selfie\\Жигуляк уголёк.jpg',
    scale=(.25, .12, .25),
    position=(-0.75, 0.43, 0)
    )
image(
    'Selfie\\жиза.jpg',
    scale=(.25, .12, .25),
    position=(-0.75, 0, 0)
    )
image(
    'Selfie\\Чёрнорабочий.jpg',
    scale=(.25, .12, .25),
    position=(-0.75, -0.43, 0)
    )

window.title = 'My Gay'
window.borderless = False
window.forced_aspect_ratio = (16, 9)
window.windowed_size = (1280, 720)
window.exit_button.visible = False
window.fps_counter.enabled = False
application.development_mode = False

app.run()
