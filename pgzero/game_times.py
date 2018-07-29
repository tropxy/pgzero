import pygame
import datetime


def get_game_time_secs():
    """
    Total runtime of the game
    :return: time elapsed in seconds
    """
    return pygame.time.get_ticks() / 1000.0


def get_game_timer():
    return str(datetime.timedelta(seconds=get_game_time_secs()))
