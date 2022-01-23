from ursina import *
from ursina.prefabs.dropdown_menu import DropdownMenu, DropdownMenuButton

app = Ursina()
window.borderless = False

a = 0

def update():
    print(a)

app.run()

