class Settings():
    # store all settings of alien invasion

    def __init__(self):
        # initilized game setting
        # screen setting
        self.screen_width = 600
        self.screen_height = 400
        self.bg_color = (230, 230, 230)
        
        # set ship's location
        self.ship_speed_factor = 1.5
        self.ship_limit = 3
        # set alien's speed
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction = 1 indicate moving right  -1 indicate moving left
        self.fleet_direction = 1

        # bullet seting
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
