import pyautogui
from io import BytesIO


def screenshot():
    src = pyautogui.screenshot()
    image_bytes = BytesIO()
    src.save(image_bytes, format='PNG')
    return image_bytes

