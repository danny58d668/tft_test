import json


def get_data(champion_name):
    file_path = 'champion_data.json'
    with open(file_path, 'r') as file:
        json_data = json.load(file)

    for entry in json_data:
        if champion_name in entry["champion"]:
            return [
                entry["champion"][0],
                entry["traits"],
                int(entry["cost"])
            ]

    return None

'''
test = get_data("Ahri")
print(test)
'''