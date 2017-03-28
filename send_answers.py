import requests
import json

url = 'http://localhost:9200/saira/sairita/1'
with open('introduction-quiz.json') as file:
	data = json.load(file)

print (data)

leer = requests.post(url, json = data)
print(leer.text)
