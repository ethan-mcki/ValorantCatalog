# import urllib.request, json 
# with urllib.request.urlopen("https://valorant-api.com/v1/weapons") as url:
#     data = json.load(url)
#     # print(data["data"][0])

# for i in data['data'][0]:
#     print(i)

# print(data['data'][2]['displayName'])
# print(data['data'][2]['category'])
# print(data['data'][2]['weaponStats']['fireRate'])


from flask import Flask, redirect, url_for, request, render_template
import requests
app = Flask(__name__)


def get_weapons():
    url = "https://valorant-api.com/v1/weapons"
    response = requests.get(url)
    return response.json()

def weapon_list():
    weapon_data = get_weapons()
    if weapon_data:
        weapons = weapon_data['data']
    else:
        weapons = []
    return weapons

weapons = weapon_list()
# Weapon item attributes:
# [0] = uuid
# [1] = displayName
# [2] = category
# [3] = defaultSkinUuid
# [4] = displayIcon
# [5] = killStreamIcon
# [6] = assetPath
# [7] = weaponStats
# [8] = shopData
# [9] = skins

# Routes to each page, Pistols, Knives, etc.
@app.route('/')
def home():
    return render_template('basic.html', weapons=weapons)

# knives, pistols, shotguns, subs, ar, lmg, snipers
@app.route('/knives.html')
def knives():
    return render_template('knives.html', weapons=weapons)

@app.route('/pistols.html')
def pistols():
    return render_template('pistols.html', weapons=weapons)

@app.route('/shotguns.html')
def shotguns():
    return render_template('shotguns.html', weapons=weapons)

@app.route('/subs.html')
def subs():
    return render_template('subs.html', weapons=weapons)

@app.route('/ar.html')
def ar(): 
    return render_template('ar.html', weapons=weapons)

@app.route('/lmg.html')
def lmg():
    return render_template('lmg.html', weapons=weapons)

@app.route('/snipers.html')
def snipers():
    return render_template('snipers.html', weapons=weapons)


if __name__ == '__main__':
    app.run(debug=True)