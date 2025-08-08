import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class about Mangaforoshian bullets"""

    def __init__(self, settings, screen, ship):
        """Create a bullet object at the ship's current position"""
        super(Bullet, self).__init__()
        self.screen = screen

        # Create a bullet rect at (0, 0) and then set correct position
        self.image = pygame.image.load('assets/bullet_bag.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = ship.rect.centerx
        self.rect.bottom = ship.rect.top

        # Store the bullet's position as a decimal value
        self.y = float(self.rect.y)
        self.speed_factor = settings.bullet_speed_factor
        # Shooting flag
        self.shooting_flag = False

    def update(self):
        """Move the bullet up to the screen"""
        # Update the decimal position of the bullet.
        self.y -= self.speed_factor
        # Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        self.screen.blit(self.image, self.rect)
