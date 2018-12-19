import sys

import pygame

def check_events():
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():  # NOTE: Our event loop, watch key events.

        if event.type == pygame.QUIT:
            sys.ext()  # NOTE: Exit the running process for our game, ie quit the game.