#! python

import pygame
from scripts.player import Player

class Level:
	
    def __init__(self, display):
		
        self.display = display
        self.all_sprites = pygame.sprite.Group()

		
    def handle_events(self, event):
        """Handles events for the level"""
  
    def update(self, dt):
        """Updates the level"""
  
    def draw(self):
        self.all_sprites.draw(self.display)


		