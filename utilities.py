import json


def download_json():
    """Загрузка данных из файла json"""
    with open("posts.json", "r", encoding='utf-8') as file:
        data = json.load(file)
    return data


def search(dic, word):
    """Поиск в словаре по слову"""
    new_list = []
    for item in dic:
        if word.lower() in item["description"].lower().split(' '):
            new_list.append(item)
    if new_list:
        return new_list
    else:
        return [{"description": "Ничего не найдено", "image": "none.jpg"}]


def save_json(description, picture_name):
    """Запись данных в файл json"""
    with open("posts.json", "r", encoding='utf-8') as file:
        data = json.load(file)
    data.append({"description": description, "image": picture_name})
    with open("posts.json", "w", encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=3)
