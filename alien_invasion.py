import sys # NOTE: Methods to interact with command line.

import pygame # NOTE: Allows us to build our game

def run_game():
    """Initialize game, create window object."""
    pygame.init() # NOTE: Initialize a pygame instance.
    screen = pygame.display.set_mode((1200, 800)) # NOTE: Set width and height of the display of the game in px, passing in a tuple.
    pygame.display.set_caption('Alien Invasion')
    bg_color = (230, 230, 230) # NOTE: Set bg color with tuple of values, RGB.

    # Start the run loop for our game.
    while True:
        for event in pygame.event.get(): # NOTE: Our event loop, watch key events.

            if event.type == pygame.QUIT:
                sys.ext() # NOTE: Exit the running process for our game, ie quit the game.

        # Redraw screen each pass of the loop and fill bg.
        screen.fill(bg_color)

        # Make the most recently drawn screen visible.
        pygame.display.flip()

# Run the game :)
run_game()