class Settings:
    """A class that initialize the game settings"""

    def __init__(self):
        """Initialize game settings"""
        # Screen settings
        self.screen_width = 2560
        self.screen_height = 1440
        self.bg_color = (230, 230, 230)
        self.back_ground_pic = "assets/BackGround.bmp"
        self.back_ground_pic2 = "assets/BackGround2.bmp"
        self.back_ground_speed = 1
        # Mangaforoshian settings
        self.mangaforoshian_speed = 2
        # Bullet settings
        self.bullet_speed_factor = 5
        self.bullet_width = 20
        self.bullet_height = 20
        # WildCats settings
        self.wild_cats_speed = 1
        # Fleet settings
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
