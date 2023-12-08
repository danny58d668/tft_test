import numpy as np



def is_bench_slot_empty(screenshot, bench_slot_coordinates):
    # Load the screenshot
    # screenshot = Image.open(screenshot)
    bench = screenshot.crop(bench_slot_coordinates)
    target_color = (154, 134, 167)  # Most frequent color
    tolerance = 20
    lower_bound = tuple(max(c - tolerance, 0) for c in target_color)
    upper_bound = tuple(min(c + tolerance, 255) for c in target_color)
    np_image = np.array(bench)
    if np_image.shape[-1] == 4:
        np_image = np_image[:, :, :3]
    mask = np.all(np_image >= lower_bound, axis=-1) & np.all(np_image <= upper_bound, axis=-1)
    count = np.sum(mask)
    total_pixels = np_image.shape[0] * np_image.shape[1]
    percentage = (count / total_pixels) * 100
    print("percentage:",percentage)
    if percentage >= 40:
        return True
    else:
        return False
'''
screenshot_path = '../img/rightbar.png'
#coord = (501, 740, 600, 830)  #  Empty
#coord = (1172, 745, 1297, 828) #  Not Empty
coord = (1295, 743, 1410, 830) #  Not Empty
result = is_bench_slot_empty(screenshot_path, coord)
if result:
    print("Bench slot is empty!")
else:
    print("Bench slot is not empty.")
'''
