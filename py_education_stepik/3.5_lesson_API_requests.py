import requests
import json
import time
import sys

'''

api_url = 'https://api.openweathermap.org/data/2.5/weather'
city = input('City? ')
prm = {
    'q': city,
    'appid': 'd01b47708dd37e3b9b580b9b978ce59b',
    'units': 'metric'
}

res = requests.get(api_url, params= prm)
#print(res.status_code)
#print(res.headers['Content-type'])
data = res.json()
print(data['main']['temp'])
template = 'Current temperature in {} is {}'
print(template.format(city, data['main']['temp']))
'''

'''
api_url = 'http://numbersapi.com/'

num = 0
#читаем из файла цифры
with open('dataset_24476_3.txt', 'r') as f:
    file = f.read().splitlines()
#отправляем запрос на каждую цифру из файла, сайту для проверки есть ли интересная информация по ней
    for i in file:
        res = requests.get(api_url+i+'/math?json=true')
        data = res.json()
        if data['found']:#проверяем в json ответе сервера параметр found
            print('Interesting')
        else:
            print('Boring')
'''

client_id = '32c7c58ad6db18b1e3dc'
client_secret = 'd5d763c84a32575d319420f63aa21941'

res = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })
js = res.json()
token = js['token']
headers = {'X-Xapp-Token': token}

end_dict = {}
list = '4d8b92b34eb68a1b2c0003f4'
with open('3.5_lesson_txt_input.txt', 'r') as f:
    list_in = f.read().splitlines()
    for list in list_in:
        res = requests.get("https://api.artsy.net/api/artists/"+list, headers=headers)
        js = res.json()
        end_dict[js['sortable_name']] = js['birthday']
        print(end_dict)
end_dict = dict(sorted(end_dict.items(), key=lambda x: (x[1], x[0])))
for i in end_dict.keys():
    print(i)