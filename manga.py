import pygame


class Manga():

    def __init__(self, settings, screen):
        """Initials mangaforoshian and set its starting position"""
        self.screen = screen
        self.settings = settings

        # Load mangaforoshian and its rect
        self.image = pygame.image.load('assets/manga_foroshian.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Place mangaforoshian at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # Store a decimal value for center of mangaforoshian
        self.centerx = float(self.rect.centerx)

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.x = 0
        self.y = 0

    def update(self):
        """Update mangaforoshian position based on movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.settings.mangaforoshian_speed * 2

        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.centerx -= self.settings.mangaforoshian_speed * 2

        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.rect.centery -= self.settings.mangaforoshian_speed * 2

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += self.settings.mangaforoshian_speed * 2

        elif pygame.mouse.get_rel() != (0, 0):
            x, y = pygame.mouse.get_pos()
            self.rect.centerx = x
            self.rect.centery = y

    def blitme(self):
        """Draw ship at its current location"""
        self.screen.blit(self.image, self.rect)
