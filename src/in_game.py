from src.slice_img import get_cards, get_gold, get_stage
from src.screenshot import screenshot
from src.move import find_orb
import pyautogui
from find_data import get_data

def in_game():
    #src = screenshot()
    src = "../img/ingame 10.png"
    cards = get_cards(src)
    gold = get_gold(src)
    stage = get_stage(src)

    print("Round ", stage[0], "Stage", stage[1])
    print("Gold: ", gold)
    print("Shop: ")
    for i in range(5):
        cards[i] = get_data(cards[i])
        print(cards[i])
    #if stage[0] == 1:
    #    stage1()
    print("----------------------------------------")

def stage1():
    find_orb()
    coordinates = [
        (570, 1000),
        (770, 1000),
        (970, 1000),
        (1171, 1000),
        (1372, 1000)
    ]
    for i in coordinates:
        pyautogui.moveTo(i)
        pyautogui.click()

in_game()