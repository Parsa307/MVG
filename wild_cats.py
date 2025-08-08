import pygame
from pygame.sprite import Sprite

class WildCats(Sprite):

    def __init__(self, settings, screen):
        """Initialize WildCats and set its starting position"""
        super(WildCats, self).__init__()
        self.screen = screen
        self.settings = settings

        # Load WildCats image and get its rect
        self.image = pygame.image.load('assets/WildCats.bmp')
        self.rect = self.image.get_rect()

        # Set each new WildCats near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw wildcat at its current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Move the WildCats to the right."""
        self.x += self.settings.wild_cats_speed * self.settings.fleet_direction
        self.rect.x = self.x
    
    def check_edges(self):
        """Return if WildCats is at edge of screen"""
        screen_rect = self.screen.get_rect()
        return self.rect.right >= screen_rect.right or self.rect.left <= 0
