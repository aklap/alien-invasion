import pygame.font
from pygame.sprite import Group


from ship import Ship

class Scoreboard():
    """A class to report scoring info."""

    def __init__(self, ai_settings, screen, stats):
        """Initialize scorekeeping attributes."""
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Font settings for scoring info
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        # Prepare the initial score and level images.
        # self.read_score()
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Turn the score into a rendered image."""
        # Round each score to the nearest 10; in Python3, it'll round to whole int
        rounded_score = round(self.stats.score, -1)
        # Insert commas between numbers
        score_str = "Score: {:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)
        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """Turn high score into rendered image."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "High Score: {:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)
        # Center high score in the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        # Draw ships left
        self.ships.draw(self.screen)

    def prep_level(self):
        """Turn level into a rendered image."""
        self.level_image = self.font.render('Current level: ' + str(self.stats.level), True, self.text_color, self.ai_settings.bg_color)
        # Position level below score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
    
    def prep_ships(self):
        """Show ships left."""
        self.ships = Group()

        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            # Create a 10px margin between ships
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    # def write_score(self):
    #     """Persist the high score by writing to file."""
    #     file_path = 'score.txt'
    #     with open(file_path, 'w') as f:
    #         f.write(str(self.stats.high_score))

    # def read_score(self):
    #     """Read score in from file."""
    #     file_path = 'score.txt'
    #     with open(file_path, 'r') as f:
    #         try:
    #             self.stats.high_score = int(f.read())
    #         except:
    #             self.stats.high_score = 0
