import sys

import pygame


def check_events(ship):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():  # NOTE: Our event loop, watch key events.

        if event.type == pygame.QUIT:
            sys.exit()  # NOTE: Exit the running process for our game, ie quit the game.
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keydown_events(event, ship)


def check_keydown_events(event, ship):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        # Move the ship rect to the right.
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # Move the ship rect to the left.
        ship.moving_left = True


def check_keyup_events(event, ship):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, ship):
    # Redraw screen each pass of the loop and fill bg.
    screen.fill(ai_settings.bg_color)
    # Draw ship
    ship.blitme()
    # Make the most recently drawn screen visible.
    pygame.display.flip()
