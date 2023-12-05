import pyautogui
import time
from src.window_title import find_in_game_window


def init_start(x, y):
    pyautogui.moveTo(x+118, y+44)  # PLAY  118 44
    pyautogui.click()
    print("PLAY")
    time.sleep(0.5)
    pyautogui.moveTo(x+760, y+300)  # Select TFT 615 242 || 760 300 for 3 mods
    pyautogui.click()
    print("TFT")
    time.sleep(0.5)
    pyautogui.moveTo(x+535, y+689)  # Create Lobby 535 689
    pyautogui.click()
    print("LOBBY")
    time.sleep(3)
    pyautogui.moveTo(x+535, y+690)  # Start Queue 535 690
    pyautogui.click()
    print("START")
    accept_queue(x+630, y+556)  # 630 556
    print("Accepted")


def accept_queue(x, y):
    print("started")
    while True:
        if find_in_game_window():
            print("done")
            break
        else:
            print("not yet")
            pyautogui.moveTo(x, y)
            pyautogui.click()
            time.sleep(2)
