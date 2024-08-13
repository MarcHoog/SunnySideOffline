import pygame

import spritesheet

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        
        # Load the spritesheet and get the first sprite image
        self.sprites = spritesheet.SpriteSheet('src/content/fonts/assets/characters/goblin/spr_idle_strip9.png', 96, 64)
        self.image = self.sprites[1]
        
        # Create the hitbox
        self.rect = self.create_center_hitbox()
        
        # DEBUG BOXES
        pygame.draw.rect(self.image, (255, 0, 0), self.rect, 1)  # Red box around the hitbox
        pygame.draw.rect(self.image, (0, 255, 0), self.image.get_rect(), 1)  # Green box around the sprite
        
        # Movement attributes
        # TODO Make this Better
        hit_box_pos = self.get_hitbox_pos() 
        offset_pos = (pos[0] - hit_box_pos[0], pos[1] - hit_box_pos[1]) 
        
        
        
        self.pos = pygame.math.Vector2(offset_pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 200
        
    # TODO Make this Better
    def get_hitbox_pos(self):
        hitbox_width = 32
        hitbox_height = 32
        hitbox_x = (self.image.get_width() - hitbox_width) / 2
        hitbox_y = (self.image.get_height() - hitbox_height) / 2
        return (hitbox_x, hitbox_y)
    
    # TODO Make this Better    
    def create_center_hitbox(self):
        # Calculate the position of the hitbox relative to the sprite
        hitbox_width = 32
        hitbox_height = 32
        hitbox_x, hitbox_y = self.get_hitbox_pos()
        hitbox_rect = pygame.Rect(hitbox_x, hitbox_y, hitbox_width, hitbox_height)
        
        return hitbox_rect

    # EVENTS    
    
    def _create_hitbox(self):
        pass
    
    def handle_events(self, event):
        """Handles events for the player"""
        
    # DELTA TIME 
        
    def update(self, dt):
        self.input()
        self.move(dt)
        
        
    def input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0
            
        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0
            
            
    def move(self, dt):
        # NOTE: Marc Hoogendoorn - What does Magnitude do?
        # When you call magnitude() on a Pygame vector, it calculates and returns the length (or magnitude) of the vector. 
        # The magnitude of a vector is the distance from the origin (0, 0) to the point represented by the vector.
        # For a 2D vector (using Vector2), if the vector is represented as (x, y), 
        # the magnitude is calculated using the Euclidean distance formula:
        # magnitude = sqrt(x^2 + y^2)
        # For the vector (3, 4):
        # magnitude = sqrt(3^2 + 4^2) = sqrt(9 + 16) = sqrt(25) = 5.0

        # NOTE: Marc Hoogendoorn - What does normalize do?
        # Normalization scales the vector to a unit vector (magnitude of 1)
        # The formula for normalization is:
        # normalized_vector = (x / magnitude, y / magnitude)
        # For the vector (3, 4), the magnitude is 5.0, so:
        # normalized_vector = (3 / 5, 4 / 5) = (0.6, 0.8)


        if self.direction.magnitude() > 0:
            self.direction.normalize()
        
        # hotizontal movement
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.x = self.pos.x # type: ignore

        
        # vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.y = self.pos.y # type: ignore

        
        
        
