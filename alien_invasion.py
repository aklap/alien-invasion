import pygame  # NOTE: Allows us to build our game
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    """Initialize game, create window object."""
    pygame.init()  # NOTE: Initialize a pygame instance.
    ai_settings = Settings()
    # Screen settings.
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # Add title to window.
    pygame.display.set_caption('Alien Invasion')
    # Make a ship.
    ship = Ship(ai_settings, screen)
    # Make bullets.
    bullets = Group()

    # Start the run loop for our game.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets()
        gf.update_screen(ai_settings, screen, ship, bullets)

# Run the game :)
run_game()
