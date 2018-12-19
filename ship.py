import pygame


class Ship():
    def __init__(self, screen):
        """Initialize the ship and set its position on the screen."""
        self.screen = screen

        # Load ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()  # NOTE: rect is the HTML rect attribute
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
