import pygame
import os



class SpriteSheet:
    """
    Class To load in an sprite sheet from an PNG file
    """
    def __init__(self, file, width, height):
        self.current_sprite = 0
        self._sprites = []
        self._width = width
        self._height = height
        self.__create_surfaces(file)
    
    def next(self):
        self.current_sprite += 1
        if self.current_sprite >= len(self):
            self.current_sprite = 0
        return self._sprites[self.current_sprite]
    
    def previous(self):
        self.current_sprite -= 1
        if self.current_sprite <= 0:
            self.current_sprite = len(self)
        return self._sprites[self.current_sprite]        
    
    def __create_surfaces(self,file):
        sheet = pygame.image.load(file).convert_alpha()
        sprite_count = 0
        for y in range(0, sheet.get_height(), self._height):
            for x in range(0, sheet.get_width(), self._width):
                sprite_count += 1
                
                sub_surface = sheet.subsurface((x, y, self._width, self._height))
                self._sprites.append(self.__double_size(sub_surface))
                
    def __double_size(self, surface):
        return pygame.transform.scale2x(surface)
    
    def __getitem__(self, sprite) -> pygame.Surface:
        return self._sprites[sprite]
    
    def __len__(self):
        return len(self._sprites)
    
    def __call__(self) -> pygame.Surface:
        return self._sprites[self.current_sprite]   
    
