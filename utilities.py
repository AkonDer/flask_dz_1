import json
import logging
from json import JSONDecodeError


class WrongFiletypeError(Exception):
    def init(self, message=None):
        super().init(message)


def download_json():
    """Загрузка данных из файла json"""
    try:
        with open("posts.json", "r", encoding='utf-8') as file:
            data = json.load(file)
            return data

    except FileNotFoundError:
        logging.exception("Файл не найден")
        return False

    except JSONDecodeError:
        logging.exception("Файл не удается преобразовать")
        return False


def search(dic, word):
    """Поиск в словаре по слову"""
    new_list = [x for x in dic if word.lower() in x["description"].lower()]

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


def check_file_type(file):
    types = [".jpg", ".png"]
    return any(x for x in types if x in file)
