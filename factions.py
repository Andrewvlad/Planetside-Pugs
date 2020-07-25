from lobby import *

factions = ['VS', 'NC', 'TR']
factions_team = []


def get_faction():
    return factions


def get_faction_team(index):
    if index >= len(factions_team):
        return None
    else:
        return factions_team[index]


def set_faction_team(faction, team):
    factions_team.insert(team, faction)
    remove(faction, factions)


def clear_faction_teams():
    global factions
    factions = ['VS', 'NC', 'TR']
    clear(factions_team)

