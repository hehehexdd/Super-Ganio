from classes.buttons.base.button import *


class Widget:
    def __init__(self):
        self.buttons = []

    def add_button(self, button: Button):
        if len(self.buttons) > 0:
            self.buttons.append(button.__class__())