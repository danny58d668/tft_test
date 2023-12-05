from PIL import Image
import pytesseract
import re
import io


def get_cards(src):
    screenshot = Image.open(src)
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
        piece = screenshot.crop((x, y, x + width, y + height))
        text = pytesseract.image_to_string(piece).split()[0].replace("‘", "")
        cards.append(text)
    return cards


def get_gold(input_path):
    screenshot = Image.open(input_path)
    gold = screenshot.crop((870, 880, 930, 910))  # get gold  832, 879, 930, 910 || 870, 880, 930, 910
    #gold = gold.convert("L")
    gold = pytesseract.image_to_string(gold,lang='eng', config='--psm 6')
    #gold = re.sub(r'^\D*', '', gold).strip()
    return gold


def get_stage(input_path):
    screenshot = Image.open(input_path)
    stage = screenshot.crop((800, 0, 875, 40))  # get stage number
    stage = pytesseract.image_to_string(stage, lang='eng', config='--psm 6').strip().split('-')
    return stage

'''
src = "../img/ingame 10.png"
s = get_stage(src)
print("Stage: ",s)
'''