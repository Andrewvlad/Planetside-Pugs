from captains import get_captain

team_pick_captain = ''


def pick_switch():
    global team_pick_captain
    if team_pick_captain == get_captain(0):
        team_pick_captain = get_captain(1)
    elif team_pick_captain == get_captain(1):
        team_pick_captain = get_captain(0)


def pick_force():
    global team_pick_captain
    team_pick_captain = get_captain(0)


def get_pick():
    return team_pick_captain


