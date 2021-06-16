import pytmx
import pygame


class Map:
    def __init__(self, filename, level):
        tm = pytmx.load_pygame(filename, pixelalpha=True)
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm
        self.level = level

    def render(self, surface):
        ti = self.tmxdata.get_tile_image_by_gid

        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                tiles = {}
                for x, y, gid, in layer:
                    tile = ti(gid)
                    if tile:
                        surface.blit(tile, (x * self.tmxdata.tilewidth, y * self.tmxdata.tileheight))
                        tiles[tile] = [x, y]
                surface_info = self.find_rect(tiles)
                self.level.surfaces[surface_info[0]] = [surface_info[1].topleft[0], surface_info[1].topleft[1]]

    def find_rect(self, tiles: dict):
        top_left = tiles[list(tiles.keys())[0]]
        size = [0, 0]

        for tile in tiles:
            tile_coords = tiles[tile]
            if tile_coords[0] < top_left[0]:
                top_left[0] = tile_coords[0]
            if tile_coords[1] < top_left[1]:
                top_left[1] = tile_coords[1]
            if (tile_coords[0] * self.tmxdata.tilewidth) > size[0]:
                size[0] = tile_coords[0] * self.tmxdata.tilewidth
            if (tile_coords[1] * self.tmxdata.tileheight) > size[1]:
                size[1] = tile_coords[1] * self.tmxdata.tileheight

        rect = pygame.Rect(top_left, size)
        surface = pygame.Surface(size)

        for tile in tiles:
            surface.blit(tile, (tiles[tile][0] * self.tmxdata.tilewidth, tiles[tile][1] * self.tmxdata.tileheight))

        return [surface, rect]

    def make_map(self):
        temp_surface = pygame.Surface((self.width, self.height))
        self.render(temp_surface)
        return temp_surface
