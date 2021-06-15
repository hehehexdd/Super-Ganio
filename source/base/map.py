import pytmx
import pygame


class Map:
    def __init__(self, filename, level):
        tm = pytmx.load_pygame(filename, pixelalpha=True)
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm
        self.level = level

    def render(self, surface, offset_x, offset_y):
        ti = self.tmxdata.get_tile_image_by_gid

        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid, in layer:
                    tile = ti(gid)

                    if tile:
                        self.level.drawables[tile] = (x * self.tmxdata.tilewidth - offset_x, y * self.tmxdata.tileheight - offset_y)
                        surface.blit(tile, (x * self.tmxdata.tilewidth,
                                            y * self.tmxdata.tileheight))

    def make_map(self, offset_x, offset_y):
        temp_surface = pygame.Surface((self.width, self.height))
        self.render(temp_surface, offset_x, offset_y)
        return temp_surface
