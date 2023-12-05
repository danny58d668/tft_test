from bs4 import BeautifulSoup

html_code = '''
<div class="rt-td" role="gridcell" style="flex: 150 0 auto; width: 150px;"><a
    class="characters-item c4 s10" href="/champions/ahri">
    <div class="character-wrapper"><img class="character-icon"
        src="https://rerollcdn.com/characters/Skin/10/Ahri.png" alt="Ahri"></div>Ahri
    </a></div>
<div class="rt-td" role="gridcell" style="flex: 150 0 auto; width: 150px;">
    <div class="characters-item trait-table">
        <div class="character-wrapper"><img class="character-icon"
                src="https://rerollcdn.com/icons/kda.png" alt="K/DA">
            <div class="d-none d-md-block" style="text-align: center;">K/DA</div>
        </div>
    </div>
</div>
<div class="rt-td" role="gridcell" style="flex: 150 0 auto; width: 150px;">
    <div class="characters-item trait-table">
        <div class="character-wrapper"><img class="character-icon"
                src="https://rerollcdn.com/icons/spellweaver.png" alt="Spellweaver">
            <div class="d-none d-md-block" style="text-align: center;">Spellweaver</div>
        </div>
    </div>
</div>
<div class="rt-td" role="gridcell" style="flex: 80 0 auto; width: 80px;">
    <div
        style="text-align: center; width: 100%; display: flex; align-items: center; justify-content: center;">
        <img class="gold-icon" src="https://rerollcdn.com/ui/icon-gold.svg" alt="cost">4
    </div>
</div>
'''

soup = BeautifulSoup(html_code, 'html.parser')

champion_item = soup.find('a', class_='characters-item')
if champion_item:
    champion_name = champion_item.text.strip()
    print(champion_name)
else:
    print("Champion not found.")