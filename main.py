from game_data.engine.base.game import *
import pygame


if __name__ == '__main__':
    #size = (1920, 1080)
    #size = (1280, 720)
    pygame.init()
    window_info = pygame.display.Info()
    size = (window_info.current_w, window_info.current_h)
    backgroundColor = 0, 0, 0
    game = Game(size, backgroundColor)
    game.start()
    exit()
