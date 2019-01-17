class Settings():
    """A class to store all settings for the game."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings.
        self.screen_width = 1200  # in px
        self.screen_height = 800  # in px
        self.bg_color = (230, 230, 230)  # NOTE: Set bg color with tuple of values, RGB.
        # Ship settings
        self.ship_speed_factor = 1.5  # Move the ship by 1.5 px
        # Bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)  # Dark gray
        self.bullets_allowed = 6
        # Speed of alien moving down
        self.fleet_drop_speed = 5
        # Limit the number of ships (lives)
        self.ship_limit = 3
        self.speedup_scale = 3
        # Increase the point values as game gets harder
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed = 3
        self.alien_speed_factor = 1.2
        # Direction flag; 1 == right, -1 == left
        self.fleet_direction = 1
        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings."""
        # Use int to round up and increase point value by whole ints
        self.alien_points = int(self.alien_points * self.score_scale)
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
