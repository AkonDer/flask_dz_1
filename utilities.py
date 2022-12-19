import json


def download_json():
    """Загрузка данных из файла json"""
    with open("posts.json", "r", encoding='utf-8') as file:
        data = json.load(file)
    return data
