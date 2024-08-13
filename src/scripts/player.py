import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,
                 pos, 
                 group,):
        super().__init__(group)
        
        self.image = pygame.Surface((32, 32))
        self.image.fill('purple')
        self.rect = self.image.get_rect(center = pos)
        
        self.direction = pygame.math.Vector2(0, 0)
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200
        
    # EVENTS    
    
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
        self.rect.centerx = self.pos.x # type: ignore

        
        # vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y # type: ignore

        
        
        
