import json

from bs4 import BeautifulSoup

# Specify the path to your HTML file
file_path = 'trimed_tft.html'

with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

# Initialize a 2D array to store the data
champion_data = []
champion_names = []
traits_list = []
costs = []

# Extracting information for each champion
champion_divs = soup.find_all('div', class_='rt-tr')


for champion_div in champion_divs:

    champion_name = champion_div.find('a', class_='characters-item').text.strip(),
    # Extract traits
    traits = [trait.text.strip() for trait in champion_div.find_all('div', class_='d-none d-md-block')]
    # Extract cost
    cost = champion_div.find('img', class_='gold-icon').next_sibling.strip()

    champion_info = {
        "champion": champion_name,
        "traits": traits,
        "cost": cost
    }

    # Add the dictionary to the list
    champion_data.append(champion_info)

print(champion_data[0])

# Save the data to a JSON file
json_path = 'champion_data.json'
with open(json_path, 'w', encoding='utf-8') as json_file:
    json.dump(champion_data, json_file, ensure_ascii=False, indent=2)
