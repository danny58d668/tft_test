import pyautogui
import pytesseract
from PIL import Image
import numpy as np

from src.empty_bench import is_slot_full
from src.screenshot import screenshot


def bench_info():
    # 110 x 85 per slot
    coordinates = [
        (422, 779),  #
        (544, 783),  #
        (662, 789),  #
        (778, 790),  #
        (890, 790),
        (890, 790),
        (1110, 790),
        (1234, 790),
        (1367, 790),
    ]
    cards = [[] for _ in range(9)]
    # Extract image slices based on provided coordinates
    for i, (x, y) in enumerate(coordinates):
        img = "../img/rightbar.png"#screenshot()
        img = Image.open(img)
        if is_slot_full(img, (x, y, x + 110, y + 85)):
            pyautogui.moveTo(x, y)  # Move the mouse to the coordinates
            pyautogui.rightClick()
            bench = img.crop((1705, 320, 1820, 345))  # get champion info
            bench = pytesseract.image_to_string(bench, lang='eng', config='--psm 6').strip()
            cards[i] = bench

    return cards


src = "../img/rightbar.png"
b = bench_info()
print(b)