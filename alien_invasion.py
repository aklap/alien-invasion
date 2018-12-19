import pygame  # NOTE: Allows us to build our game

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    """Initialize game, create window object."""
    pygame.init()  # NOTE: Initialize a pygame instance.
    ai_settings = Settings()
    # Screen settings.
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    # Make a ship
    ship = Ship(screen)

    # Start the run loop for our game.
    while True:
        gf.check_events()
        # Redraw screen each pass of the loop and fill bg.
        screen.fill(ai_settings.bg_color)

        # Draw ship
        ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

# Run the game :)
run_game()
