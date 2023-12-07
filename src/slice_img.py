import pyautogui
from PIL import Image
import pytesseract
from screenshot import screenshot
from find_data import get_data

def get_cards(src):
    img = Image.open(src)
    coordinates = [
        (480, 1040),  # 480 1040 -> 630 1070   150 30
        (680, 1040),  # 680
        (880, 1040),  # 885
        (1080, 1040),  # 1085
        (1285, 1040)  # 1285
    ]
    cards = []
    # Extract image slices based on provided coordinates
    for i, (x, y) in enumerate(coordinates):
        width, height = 150, 30
        piece = img.crop((x, y, x + width, y + height))
        text = pytesseract.image_to_string(piece).split()[0].replace("‘", "")
        cards.append(text)
    for i in range(5):
        cards[i] = get_data(cards[i])
    return cards


def get_gold(input_path):
    img = Image.open(input_path)
    gold = img.crop((870, 880, 930, 910))  # get gold  832, 879, 930, 910 || 870, 880, 930, 910
    #gold = gold.convert("L")
    gold = pytesseract.image_to_string(gold,lang='eng', config='--psm 6')
    #gold = re.sub(r'^\D*', '', gold).strip()
    return gold


def get_stage(input_path):
    img = Image.open(input_path)
    stage = img.crop((800, 0, 875, 40))  # get stage number stage 2 above: 740 0 815 0
    stage = pytesseract.image_to_string(stage, lang='eng', config='--psm 6').strip().split('-')
    return stage


def bench_info():
    # 1070 320 1859 345
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
    cards = []
    # Extract image slices based on provided coordinates

    for i, (x, y) in enumerate(coordinates):
        img = screenshot()
        img = Image.open(img)
        pyautogui.moveTo(x, y)  # Move the mouse to the coordinates
        pyautogui.rightClick()
        bench = img.crop((1705, 320, 1820, 345))  # get champion info
        bench = pytesseract.image_to_string(bench, lang='eng', config='--psm 6').strip()
        cards.append(bench)

    return cards


'''
src = "../img/rightbar.png"
t = "../img/ingame 10.png"
s = get_stage(src)
print("Stage: ",s)
b = bench_info(src)
print(b)
v = bench_info(t)
print(v)
'''
test = bench_info()
print(test)