import pygame
from pygame.sprite import Group
import game_functions
from game_functions import WildCatsFleet
from settings import Settings
from manga import Manga
import time

def run_game():
    """Initialize game and create screen object"""
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height), pygame.FULLSCREEN)

    # Set mangaforoshian
    mangaforoshian = Manga(settings, screen)
    # Make a group of bullets and a group of WildCats.
    bullets = Group()
    wild_cats = Group()

    # Set background image
    bg_img = pygame.image.load(settings.back_ground_pic)
    bg_img = pygame.transform.scale(bg_img, (settings.screen_width, settings.screen_height))
    bg_img2 = pygame.image.load(settings.back_ground_pic2)
    bg_img2 = pygame.transform.scale(bg_img2, (settings.screen_width, settings.screen_height))

    # Make a fleet of WildCats
    game_functions.create_fleet(settings, screen, wild_cats)
    # WildCats fleet
    wild_cats_fleet = WildCatsFleet(settings, wild_cats)
    # Start the main loop for game
    screen_mover = [0]
    pic_1_j = [0]
    pic_2_j = [-settings.screen_height]
    n = [1]
    shooting_flag = [False, time.time()]
    pygame.mouse.set_pos([settings.screen_width / 2, settings.screen_height])
    while True:
        # Watch for mouse and keyboard events
        game_functions.check_events(settings, screen, mangaforoshian, bullets, shooting_flag)
        wild_cats.update()
        wild_cats_fleet.check_fleet_edges()
        mangaforoshian.update()
        bullets.update()

        # Get rid of bullets that have been disappeared
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)

        game_functions.update_screen(screen, bg_img, bg_img2, mangaforoshian, wild_cats, bullets, n, pic_1_j, pic_2_j, screen_mover, settings.back_ground_speed)


run_game()
