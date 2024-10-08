import sys
import pygame
import logging

from logger import setup_logger
from scripts.player import Player
from scripts.level import Level
from events import ANIMATE

class GameClient:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Sunny Side")
        
        self.screen = pygame.display.set_mode((1280, 960))

        self.display = pygame.Surface((640, 480))
        self.clock = pygame.time.Clock()
        self.level = Level(self.display)
        self.player_sprites = pygame.sprite.Group()
        self.player = Player((0, 0), self.player_sprites) 
        
        self.entities = {'player': self.player} 
    
    
    def run(self):
        
        while True:
            self.display.fill((0, 0, 0))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Quiting the Game.")
                    pygame.quit()
                    sys.exit()
                if event.type == ANIMATE:
                    self.entities[event.entity].handle_events(event)

            dt = self.clock.tick() / 1000

            self.player_sprites.update(dt)      
            self.level.update(dt) 

            self.player_sprites.draw(self.display)
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0,0))
            pygame.display.update()
            
if __name__ == "__main__":
    GameClient().run()