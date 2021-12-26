scenes = []
LoadScene = []
SecondScene = []
scenes.append(LoadScene)
scenes.append(SecondScene)
def change_scene(off, on):
    for i in off:
        i.disable()
    for i in on:
        i.enable()

def load2game():
    change_scene(LoadScene, SecondScene)