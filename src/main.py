import sys
import pygame
import logging

from logger import setup_logger
from scripts.player import Player
from scripts.level import Level

class GameClient:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Sunny Side")
        
        self.screen = pygame.display.set_mode((1280, 960))
  #      self.font = pygame.font.Font('./src/client/content/fonts/Maplestory Bold.ttf', 20)

        self.display = pygame.Surface((1280, 960))
        self.clock = pygame.time.Clock()

        self.level = Level(self.display)
        
        self.player_sprites = pygame.sprite.Group()
        self.player = Player((640, 360), self.player_sprites) 
    
    
    def run(self):
        
        while True:
            self.display.fill((0, 0, 0))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Quiting the Game.")
                    pygame.quit()
                    sys.exit()
                
                    


            dt = self.clock.tick() / 1000

            self.player_sprites.update(dt)      
            self.level.update(dt) 

            self.player_sprites.draw(self.display)
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0,0))
            pygame.display.update()
            
if __name__ == "__main__":
    GameClient().run()