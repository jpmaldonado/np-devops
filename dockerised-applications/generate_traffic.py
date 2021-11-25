import requests
import random

url = 'http://127.0.0.1:5000/buy/{}'

for i in range(10000):
    random_item = random.randint(1,6)
    requests.get(url.format(i))