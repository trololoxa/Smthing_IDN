from ursina import Entity, camera

def disableScene(inputScene):
    for i in inputScene:
        i.disable()
def enableScene(inputScene):
    for i in inputScene:
        i.enable()


class Image(Entity):
    def __init__(self, texture, **kwargs):
        super().__init__(
            parent=camera.ui,
            model='quad',
            texture=texture,
            **kwargs
            )
