import time
import pyautogui

'''
Walk for Orbs:
549, 680
612, 200
1257, 200
1257, 680
'''
def find_orb():
    # Coordinates
    coords = [(549, 680), (612, 200), (1257, 200), (1257, 680)]
    for x, y in coords:
        pyautogui.moveTo(x, y)  # Move the mouse to the coordinates
        pyautogui.rightClick()  # Simulate right-click
        time.sleep(3)

