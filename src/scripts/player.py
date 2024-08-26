import pygame

import spritesheet
import timer
import config
import random

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        
        self.stance = 'idle'
        self.pos = pygame.Vector2(pos)
        
        # Load the spritesheet and get the first sprite image
        self.assets = self.load_assets()
        self.image = self.assets[self.stance]()
 
        # Calculate the offset for the image so the image is centered ('These images have allot of empty space, for animations')
        self.offset = self.image_center_offset()

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = -self.offset 
        self.hitbox = pygame.Rect(self.pos.x, self.pos.y, config.PLAYER_HITBOX_WIDTH, config.PLAYER_HITBOX_HEIGHT)                          
       
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 200
        
        self.flip = False
        
        self.animation_timer = timer.Timer(300, self.animate)
        self.animation_timer.start()
        
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
        
    def image_center_offset(self):
        """Determine the hitbox coordinates so the Hitbox is centered on the sprite"""    
        hitbox_x = (self.image.width - config.PLAYER_HITBOX_WIDTH) / 2 # type: ignore
        hitbox_y = (self.image.height - config.PLAYER_HITBOX_HEIGHT) / 2 # type: ignore
        return pygame.Vector2((hitbox_x, hitbox_y))   
    
    def handle_stance(self):
        """Handle the stance of the player"""
        if self.direction.magnitude() > 0:
            self.stance = 'walk'
        else:
            self.stance = 'idle'
    
    def handle_events(self, event):
        pass        
        
    def update(self, dt):
        """Update the player based on Delta Time""" 
        self.input()
        self.move(dt)
        self.handle_stance()
        self.animation_timer.update(dt)
        
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
            print('differnt stance')    
            self.stance = random.choice(list(self.assets.keys()))
            print(self.stance)
            
    def move(self, dt):
        """Move the player based on the direction and speed"""  

        if self.direction.magnitude() > 0:
           self.direction = self.direction.normalize()
        
        # hotizontal movement
        self.pos.x += self.direction.x * self.speed * dt
        self.hitbox.x = self.pos.x
        self.rect.x = self.pos.x - self.offset.x # type: ignore

        # vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        self.hitbox.y = self.pos.y
        self.rect.y = self.pos.y - self.offset.y # type: ignore