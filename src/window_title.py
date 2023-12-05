import pygetwindow as gw


def find_lol_window():
    lol_windows = gw.getWindowsWithTitle('League of Legends')
    if lol_windows:
        window = lol_windows[0]
        lol_windows[0].activate()
        return window.left, window.top
    else:
        return None



def find_in_game_window():
    lol_windows = gw.getWindowsWithTitle('League of Legends (TM) Client')
    if lol_windows:
        return True
    else:
        return False


