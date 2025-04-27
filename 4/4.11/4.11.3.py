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
        watch +=int(item["count"])
    elif item['categories'] == 'mobile':
        mobile +=int(item["count"])
    elif item['categories'] == 'mouse':
        mouse +=int(item["count"])
    elif item['categories'] == 'hdd':
        hdd +=int(item["count"])
    elif item['categories'] == 'headphones':
        headphones +=int(item["count"])
print(f"'watch': {watch}, 'mobile': {mobile}, 'mouse': {mouse}, 'hdd': {hdd}, 'headphones': {headphones}")

{'watch': 853, 'mobile': 820, 'mouse': 2692, 'hdd': 1273, 'headphones': 1006}