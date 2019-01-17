"""A class to represent game statistics."""
class Stats():
    """Hold state about a game instances stats."""
    def __init__(self, ai_settings):
        """Initialize stats"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        """Initialize the stats that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        # Never reset the high score!
        self.high_score = self.read_score()
        self.level = 1
    
    def write_score(self):
        """Persist the high score by writing to file."""
        file_path = 'score.txt'
        with open(file_path, 'w') as f:
            f.write(str(self.high_score))

    def read_score(self):
        """Read score in from file."""
        file_path = 'score.txt'
        
        with open(file_path, 'r') as f:
            score = f.read()

            if score == '':
                return 0
            else:
                return int(score)
