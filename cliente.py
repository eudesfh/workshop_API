import requests

# vou testar utilizando a url local :)

URL = "http://127.0.0.1:8000/recursos" # url gerada pelo render após deploy ou local

response = requests.get(URL)
print(response.text)



