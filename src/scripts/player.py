import pygame

import spritesheet
import timer
import config
import random

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        
        self.state = 'idle'
        self.default_state = 'idle'
        self.pos = pygame.Vector2(pos)
        
        # Load the spritesheet and get the first sprite image
        self.assets = self.load_assets()
        self.image = self.assets[self.state]()
 
        # Calculate the offset for the image so the image is centered ('These images have allot of empty space, for animations')
        self.offset = self.image_center_offset()

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = -self.offset 
        self.hitbox = pygame.Rect(self.pos.x, self.pos.y, config.PLAYER_HITBOX_WIDTH, config.PLAYER_HITBOX_HEIGHT)                          
       
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 200
        
        self.flip = False
        self.cooldown = False    
        
        self.animation_timer = timer.Timer(300, True, self.animate)
        self.animation_timer.start()
        self.action_cooldown = timer.Timer(1000, False, lambda: setattr(self, 'cooldown', False))    
        self.state_queue = []
        
    def animate(self):
        """Animate the player sprite"""
        self.assets[self.state].next()
        self.image = self.assets[self.state]()
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
        if self.state in {'idle'} and self.direction.magnitude() > 0:
            self.state_queue.append('walk')

        if self.state == 'walk' and self.direction.magnitude() == 0:
            self.state_queue.pop()  

        if self.state not in {'idle', 'walk'} and self.direction.magnitude() > 0:
            self.state_queue.pop()
            # Cancel The Action by sending an Event to the Action Object
            
            
        if len(self.state_queue) != 0:
            self.state = self.state_queue[-1]
        else: 
            self.state = self.default_state     
    
    
    def handle_events(self, event):
        pass        
        
    def update(self, dt):
        """Update the player based on Delta Time""" 
        self.input()
        self.move(dt)
        self.handle_stance()
        self.animation_timer.update(dt)
        self.action_cooldown.update(dt)
        
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
            if not self.cooldown:
                self.state_queue.append(random.choice(list(self.assets.keys())))
                self.cooldown = True
                self.action_cooldown.start()
            
            
        if keys[pygame.K_BACKSPACE]:
            if not self.cooldown:
                self.cooldown = True
                self.action_cooldown.start()
                if len(self.state_queue) != 0:      
                    self.state_queue.pop()
            
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