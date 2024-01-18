# import urllib.request, json 
# with urllib.request.urlopen("https://valorant-api.com/v1/weapons") as url:
#     data = json.load(url)
#     # print(data["data"][0])

# for i in data['data'][0]:
#     print(i)

# print(data['data'][2]['displayName'])
# print(data['data'][2]['category'])
# print(data['data'][2]['weaponStats']['fireRate'])


from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()