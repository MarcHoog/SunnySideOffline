import pygame

import spritesheet
import config
from events import ANIMATE

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        
        self.stance = 'mining'
        
        # Load the spritesheet and get the first sprite image
        self.assets = self.load_assets()
        self.image = self.assets[self.stance]()
        self.rect = self._create_hitbox()
        self.flip = False
        
        self.pos = pygame.math.Vector2(self._offset_player_pos(pos))
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 200
        
        pygame.event.post(pygame.event.Event(ANIMATE, {'entity': 'player'}))
        
    def animate(self):
        """Animate the player sprite"""
        self.assets[self.stance].next()
        self.image = self.assets[self.stance]()
        if self.flip:
            self.image = pygame.transform.flip(self.image, True, False)
      
    def load_assets(self):
        assets = {}
        
        for stance in config.PLAYER_STATES:
            assets[stance] = spritesheet.SpriteSheet(f'src/content/assets/characters/goblin/{stance}.png', 
                                               config.PLAYER_SRITE_SHEET_SPRITE_WIDTH, 
                                               config.PLAYER_SPRITE_SHEET_SPRITE_HEIGHT)        
        return assets
        
    def determine_hitbox_cords(self):
        """Determine the hitbox coordinates so the Hitbox is centered on the sprite"""    
        hitbox_x = (self.image.get_width() - config.PLAYER_HITBOX_WIDTH) / 2 # type: ignore
        hitbox_y = (self.image.get_height() - config.PLAYER_HITBOX_HEIGHT) / 2 # type: ignore
        return (hitbox_x, hitbox_y)

    def _offset_player_pos(self, pos):
        """ Offset the player position so the hitbox is centered on the sprite and the Player is drawn from the top left corner of the Hitbox"""     
        hit_box_pos = self.determine_hitbox_cords() 
        offset_pos = (pos[0] - hit_box_pos[0], pos[1] - hit_box_pos[1]) 
        return offset_pos
    
    def _create_hitbox(self):
        """ Create a hitbox for the player sprite """
        # Calculate the position of the hitbox relative to the sprite
        hitbox_x, hitbox_y = self.determine_hitbox_cords()
        hitbox_rect = pygame.Rect(hitbox_x, hitbox_y, config.PLAYER_HITBOX_WIDTH, config.PLAYER_HITBOX_HEIGHT) 
        return hitbox_rect

    def handle_events(self, event):
       if event.type == ANIMATE:
           self.animate()
           pygame.time.set_timer(pygame.event.Event(ANIMATE, {'entity': 'player'}), 100)
        
        
    def update(self, dt):
        """Update the player based on Delta Time""" 
        self.input()
        self.move(dt)
        
    def input(self):
        """Handle the input for the player"""
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0
            
        if keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.flip = True
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.flip = False
        else:
            self.direction.x = 0
            
        if keys[pygame.K_SPACE]:
            self.animate()
            
            
    def move(self, dt):
        """Move the player based on the direction and speed"""  

        if self.direction.magnitude() > 0:
           self.direction = self.direction.normalize()
        
        # hotizontal movement
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.x = self.pos.x # type: ignore

        
        # vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.y = self.pos.y # type: ignore

        
        
        
