import pytesseract
from src.start_game import init_start
from src.window_title import find_lol_window
from src.in_game import in_game


def main():
    pytesseract.tesseract_cmd = r'D:\App\Tesseract\tesseract.exe'
    print("Start server:")
    client_x, client_y = find_lol_window()
    #ID 1130 30 -> 1250 50

    print(client_x, client_y)
    init_start(client_x, client_y)  # Start game at first time

    while True:
        in_game()


main()
