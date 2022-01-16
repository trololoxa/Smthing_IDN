from ursina import *
from ursina.prefabs.dropdown_menu import DropdownMenu, DropdownMenuButton

app = Ursina()
window.borderless = False
files = []
for i in range(len()):
    files.append(DropdownMenuButton('a' + str(i)))
a = 0

def update():
    print(a)

app.run()

