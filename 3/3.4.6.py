from lib import *

p =int(-50)
print(p)

response = requests.get('https://parsinger.ru/3.4/1/json_weather.json')

j = response.json()

print(j)
list_m = {}
min_t = -20
for el in j:
    temperatura = el['Температура воздуха']
    val = temperatura[:-2]
    key = el['Дата']
    val = int(val)
    if min_t>val:
        min_t = val
        print(min_t)
    list_m[val] = key

print(min_t)
print(list_m[min_t])