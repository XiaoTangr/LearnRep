class GameStats():
    def __init__(self,opts):
        self.opts = opts
        self.game_active = False
        self.reset_stats()


    def reset_stats(self):
        self.ships_left = self.opts.ship_limit
        
    