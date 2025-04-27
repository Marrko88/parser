import requests

url = 'https://parsinger.ru/downloads/get_json/res.json'

response = requests.get(url=url).json()
watch = 0
mobile = 0
mouse = 0
hdd = 0
headphones= 0
for item in response:
    if item['categories'] == 'watch':
        watch += int(item["count"]) * int(item["price"].split(" ")[0])
    elif item['categories'] == 'mobile':
        mobile +=int(item["count"]) * int(item["price"].split(" ")[0])
    elif item['categories'] == 'mouse':
        mouse += int(item["count"]) * int(item["price"].split(" ")[0])
    elif item['categories'] == 'hdd':
        hdd += int(item["count"]) * int(item["price"].split(" ")[0])
    elif item['categories'] == 'headphones':
        headphones += int(item["count"]) * int(item["price"].split(" ")[0])

mass = {
    'watch': watch,
    'mobile': mobile,
    'mouse': mouse,
    'hdd': hdd,
    'headphones': headphones
}
print(mass)

