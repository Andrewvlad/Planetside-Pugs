from match import *
from update import *

captains = []


def get_captain(index):
    if index >= len(captains):
        return f'BuggedCaptain#{index + 1}'
    else:
        return captains[number]


def set_captain(player):
    add(player, captains)
    remove_match(player)


def remove_captain(player):
    remove(player, captains)


def clear_captains():
    clear(captains)
