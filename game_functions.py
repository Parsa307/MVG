import sys
import time

import pygame
from settings import Settings
from bullet import Bullet
from wild_cats import WildCats


def check_keydown_event(event, mangaforoshian, shooting_flag):
    """Response to hold keys"""
    if event.key == pygame.K_RIGHT:
        # Move mangaforoshian to the right
        mangaforoshian.moving_right = True
    elif event.key == pygame.K_LEFT:
        # Move mangaforoshian to the left
        mangaforoshian.moving_left = True
    elif event.key == pygame.K_UP:
        # Move mangaforoshian to the up
        mangaforoshian.moving_up = True
    elif event.key == pygame.K_DOWN:
        # Move mangaforoshian to the down
        mangaforoshian.moving_down = True
    elif event.key == pygame.K_SPACE:
        shooting_flag[0] = True
    elif event.key == pygame.K_ESCAPE:
        sys.exit()


def check_mousedown_event(event, shooting_flag):
    """Response to clicking mouse"""
    if event.button == 1:
        shooting_flag[0] = True


def check_mouseup_event(event, shooting_flag):
    """Response to clicking mouse"""
    if event.button == 1:
        shooting_flag[0] = False


def check_keyup_event(event, mangaforoshian, shooting_flag):
    if event.key == pygame.K_RIGHT:
        # Stop moving mangaforoshian to the right
        mangaforoshian.moving_right = False
    elif event.key == pygame.K_LEFT:
        # Stop moving mangaforoshian to the left
        mangaforoshian.moving_left = False
    elif event.key == pygame.K_UP:
        # Stop moving mangaforoshian to the up
        mangaforoshian.moving_up = False
    elif event.key == pygame.K_DOWN:
        # Stop moving mangaforoshian to the down
        mangaforoshian.moving_down = False
    elif event.key == pygame.K_SPACE:
        shooting_flag[0] = False


def adding_bullets(settings, screen, mangaforoshian, bullets):
    # Create a new bullet and add it to the bullets group.
    new_bullet = Bullet(settings, screen, mangaforoshian)
    bullets.add(new_bullet)

def check_events(settings, screen, mangaforoshian, bullets, shooting_flag):
    """Respond to keypress and mouse"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, mangaforoshian, shooting_flag)

        elif event.type == pygame.KEYUP:
            check_keyup_event(event, mangaforoshian, shooting_flag)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            check_mousedown_event(event, shooting_flag)

        elif event.type == pygame.MOUSEBUTTONUP:
            check_mouseup_event(event, shooting_flag)
        if shooting_flag[0] and time.time() - shooting_flag[1] > .25:
            adding_bullets(settings, screen, mangaforoshian, bullets)
            shooting_flag[1] = time.time()


settings = Settings()


def update_screen(screen, bg_img, bg_img2, manga, wild_cats, bullets, n, pic_1_j, pic_2_j, screen_mover, speed=1):
    screen.fill((255, 255, 255))
    screen.blit(bg_img, (0, pic_1_j[0] + screen_mover[0]))
    screen.blit(bg_img2, (0, pic_2_j[0] + screen_mover[0]))
    if screen_mover[0] != 0 and screen_mover[0] % settings.screen_height == 0:
        if n[0] % 2 == 1:
            pic_1_j[0] = -settings.screen_height
            pic_2_j[0] = 0
            screen_mover[0] = 0
        else:
            pic_2_j[0] = -settings.screen_height
            pic_1_j[0] = 0
            screen_mover[0] = 0
        n[0] += 1
    screen_mover[0] += speed
    # Redraw all bullets behind mangaforoshian and enemies
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # Redraw draw screen during each pass through the loop
    wild_cats.draw(screen)
    manga.blitme()
    pygame.mouse.set_visible(False)
    pygame.display.update()
    # Make most recently drawn screen visible
    pygame.display.flip()
    # Check for any bullets that have hit enemies
    # If so we get rid of the bullet and enemies
    collisions = pygame.sprite.groupcollide(bullets, wild_cats, True, True)


def get_numbers_wild_cats_x(settings, wild_cats_width):
    """Determine the number of wild cats that fit in a row"""
    available_space_x = settings.screen_width - 2 * wild_cats_width
    numbers_wild_cats_x = int(available_space_x / (2 * wild_cats_width))
    return numbers_wild_cats_x

def get_numbers_wild_cats_y(settings, wild_cats_height):
      """Determine the number of wild cats that fit in a row"""
      available_space_y = settings.screen_height - 3 * wild_cats_height
      numbers_wild_cats_y = int(available_space_y / (2 * wild_cats_height))
      return numbers_wild_cats_y

def create_wild_cats(settings, screen, wild_cats, col_index, row_index):
    """Create a wild cats and place it in the row"""
    wild_cat = WildCats(settings, screen)
    wild_cats_width = wild_cat.rect.width
    wild_cats_height = wild_cat.rect.height
    wild_cat.rect.x = wild_cats_width + 2 * wild_cats_width * col_index
    wild_cat.rect.y = wild_cats_height + 2 * wild_cats_height * row_index
    wild_cats.add(wild_cat)

def create_fleet(settings, screen, wild_cats):
    """Create a full fleet of WildCats"""
    # Create wild cat and find the number of wild cats in a row
    wild_cat = WildCats(settings, screen)
    numbers_wild_cats_x = get_numbers_wild_cats_x(settings, wild_cat.rect.width)
    numbers_wild_cats_y = get_numbers_wild_cats_y(settings, wild_cat.rect.height)

    # Loop through rows and columns to place WildCats correctly
    for row_index in range(numbers_wild_cats_y):
        for col_index  in range(numbers_wild_cats_x):
            create_wild_cats(settings, screen, wild_cats, col_index, row_index)

class WildCatsFleet:
    def __init__(self, settings, wild_cats_group):
        self.settings = settings
        self.wild_cats_group = wild_cats_group

    def check_fleet_edges(self):
        for wild_cat in self.wild_cats_group.sprites():
            if wild_cat.check_edges():
                self.change_fleet_direction()
                break

    def change_fleet_direction(self):
        """Change the fleet's direction."""
        self.settings.fleet_direction *= -1
