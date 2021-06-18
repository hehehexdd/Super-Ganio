from source.buttons.base.button import *
import pygame


class Widget:
    def __init__(self, start_pos: tuple = (0, 0),
                 space_between_items: float = 0,
                 space_between_title_and_first_item: float = 0,
                 title_text: str = "",
                 text_size: int = 18,
                 text_color: tuple = (255, 255, 255),
                 owner: object = None):

        self.buttons = []
        self.start_pos = start_pos
        self.text_pos = self.start_pos
        self.space_between_items = space_between_items
        self.space_between_title_and_first_item = space_between_title_and_first_item
        self.owner = owner
        self.text = None

        if len(title_text) > 0:
            self.text = pygame.font.SysFont('arial', text_size, True).render(title_text, True, text_color)
            self.start_pos = (self.start_pos[0], self.start_pos[1] + (self.text.get_rect().height / 2) + self.space_between_title_and_first_item + 10)

    def add_button(self, button: Button):
        if len(self.buttons) > 0:
            last_button_rect = self.buttons[len(self.buttons) - 1].get_rect()
            new_pos = (last_button_rect.centerx, last_button_rect.centery + (last_button_rect.height / 2) + self.space_between_items)
            #re-setup button with new position
            button.setup(button.arguments_passed[0],
                         button.arguments_passed[1],
                         button.arguments_passed[2],
                         button.arguments_passed[3],
                         button.arguments_passed[4],
                         button.arguments_passed[5],
                         new_pos,
                         button.arguments_passed[7],
                         button.arguments_passed[8],
                         button.arguments_passed[9])
        else:
            button.setup(button.arguments_passed[0],
                         button.arguments_passed[1],
                         button.arguments_passed[2],
                         button.arguments_passed[3],
                         button.arguments_passed[4],
                         button.arguments_passed[5],
                         self.start_pos,
                         button.arguments_passed[7],
                         button.arguments_passed[8],
                         button.arguments_passed[9])
        self.buttons.append(button)

    def draw(self, renderer: pygame.surface.Surface):
        if self.text is not None:
            renderer.blit(self.text, self.text.get_rect(center=self.text_pos))
        for button in self.buttons:
            button.draw(renderer)

    def handle_event(self, event: ButtonEvent, mouse_pos: tuple):
        for button in self.buttons:
            button.handle_event(event, mouse_pos)