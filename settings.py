class Settings():
    """A class to store all settings for the game."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings.
        self.screen_width = 1200  # in px
        self.screen_height = 800  # in px
        self.bg_color = (230, 230, 230)  # NOTE: Set bg color with tuple of values, RGB.
