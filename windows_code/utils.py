import requests


def load_json():
    data = requests.get('https://api.npoint.io/f79067bb7db852d674da')
    data_words = data.json()
    return data_words


libre_dt = load_json()

print(libre_dt)