from engine.buttons.base.button import *


class BackButtonWidget(Button):
    def __init__(self,
                 should_create_text: bool = True,
                 should_create_background: bool = False,
                 text: str = "",
                 text_size: int = 18,
                 text_color=(233, 233, 233, 255),
                 text_hover_color=(255, 255, 255, 255),
                 position = (0, 0),
                 background_color=(127, 127, 127, 255),
                 background_hover_color=(177, 177, 177, 255),
                 background_size = (100, 100),
                 owner: object = None,
                 custom_data = None):

        super().__init__(should_create_text, should_create_background, text, text_size, text_color, text_hover_color,
                         position, background_color, background_hover_color, background_size, owner, custom_data)

    def on_click(self):
        if self.custom_data:
            self.owner.set_widget(self.custom_data[0])