# import urllib.request, json 
# with urllib.request.urlopen("https://valorant-api.com/v1/weapons") as url:
#     data = json.load(url)
#     # print(data["data"][0])

# for i in data['data'][0]:
#     print(i)

# print(data['data'][2]['displayName'])
# print(data['data'][2]['category'])
# print(data['data'][2]['weaponStats']['fireRate'])



# @app.route('/')
# def hello():
#     return 'Hello World!'

from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('basic.html')

# knives, pistols, shotguns, subs, ar, lmg, snipers
@app.route('/knives.html')
def knives():
    return render_template('knives.html')

@app.route('/pistols.html')
def pistols():
    return render_template('pistols.html')

@app.route('/shotguns.html')
def shotguns():
    return render_template('shotguns.html')

@app.route('/subs.html')
def subs():
    return render_template('subs.html')

@app.route('/ar.html')
def ar(): 
    return render_template('ar.html')

@app.route('/lmg.html')
def lmg():
    return render_template('lmg.html')

@app.route('/snipers.html')
def snipers():
    return render_template('snipers.html')


if __name__ == '__main__':
    app.run(debug=True)