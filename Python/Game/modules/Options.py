#################################################
# File Name:Options.py
# Desc:The global options of game
# auther: TJRdのTanga
#################################################

class Options():
    def __init__(self):
        
        # evn param,enmu of "prod" or "dev"
        self.evn = "dev"

        # the options of Windows
        self.screen_width=1024
        self.screen_height= 768
        self.bg_color = (230,230,230)

        # the options of ship
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # the options of bullet
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = -1
        # bullets keep display after shoted aliens if = true
        self.bullets_keep= True


        # the options of alien
        self.alien_space_x_multiple = 2
        self.alien_space_y_multiple = 1.2
        self.alien_speed_factor = 1
        # drop speed of alien
        self.alien_drop_speed =100 
        # run direction to right is 1 ,left is -1
        self.alien_direction = 1


        self.speedup_scale = 1.1
        self.initaliize_dynamic_speed = 1.0


    def initialize_dynamic_settings(self):
        self.alien_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.ship_speed_factor = 1
        self.alien_direction = 1
        
    def increase_speed(self):
        self.alien_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.ship_speed_factor *= self.speedup_scale
    