import sys

import pygame


def check_events():
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():  # NOTE: Our event loop, watch key events.

        if event.type == pygame.QUIT:
            sys.ext()  # NOTE: Exit the running process for our game, ie quit the game.


def update_screen(ai_settings, screen, ship):
    # Redraw screen each pass of the loop and fill bg.
    screen.fill(ai_settings.bg_color)
    # Draw ship
    ship.blitme()
    # Make the most recently drawn screen visible.
    pygame.display.flip()
