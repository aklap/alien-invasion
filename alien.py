import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""
    def __init__(self, ai_settings, screen):
        """Initialize an instance of Alien and set position."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load alien image and set rect attr.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each alien near top left corner of window
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store alien's exact position
        self.x = float(self.rect.x)

        # Speed of alien moving right or left
        self.alien_speed_factor = 1
        # Speed of alien moving down
        self.fleet_drop_speed = 10
        # Direction flag; 1 == right, -1 == left
        self.fleet_direction = 1

    def update(self):
        """Move alien to the right."""
        # Increase x of sprite by speed factor
        self.x += self.alien_speed_factor
        # Assign new value of x to alien rect
        self.rect.x = self.x

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)
