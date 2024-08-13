import pygame
import os



class SpriteSheet:
    """
    Class To load in an sprite sheet from an PNG file
    """
    def __init__(self, file, width, height):
        self._sprites = {}
        self._width = width
        self._height = height
        self.__create_surfaces(file)
        
    
    def __create_surfaces(self,file):
        sheet = pygame.image.load(file).convert_alpha()
        sprite_count = 0
        for y in range(0, sheet.get_height(), self._height):
            for x in range(0, sheet.get_width(), self._width):
                sprite_count += 1
                
                sub_surface = sheet.subsurface((x, y, self._width, self._height))
                self._sprites[sprite_count] = self.__double_size(sub_surface)
                
    def __double_size(self, surface):
        return pygame.transform.scale2x(surface)
    
    def __getitem__(self, sprite) -> pygame.Surface:
        return self._sprites[sprite]
    
    def __len__(self):
        return len(self._sprites)