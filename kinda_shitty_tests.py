from ursina import *
from ursina.prefabs.dropdown_menu import DropdownMenu, DropdownMenuButton

class a:
    def __init__(self, a, **kwargs):
        self.a = a
        self.kwargs = kwargs

    def print_a(self):
        print(self.a)

    def print_kwargs(self):
        print(self.kwargs)
        for key, value in self.kwargs.items():
            print(key, value)

aa = a(a=6, b=5, c='a')
aa.print_a()
aa.print_kwargs()
