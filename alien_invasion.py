import pygame  # NOTE: Allows us to build our game
from pygame.sprite import Group
from settings import Settings
from game_stats import Stats as GameStats
from ship import Ship
import game_functions as gf
from button import Button

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
    # Group aliens.
    aliens = Group()

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Initalize stats for a new game
    stats = GameStats(ai_settings)

    # Start the run loop for our game.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
            gf.update_screen(ai_settings, screen, ship, aliens, bullets)
        else:
            print('game is over')
# Run the game :)
run_game()
