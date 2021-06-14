from classes.base import game

if __name__ == '__main__':
    size = (1280, 720)
    backgroundColor = 0, 0, 0

    gameInstance = game.Game(size, backgroundColor)
    gameInstance.start()
    exit()
