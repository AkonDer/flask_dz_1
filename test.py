data = [
    {
        "description": "Китайская еда",
        "image": "china.jpg"
    },
    {
        "description": "Русская еда",
        "image": "russian.jpg"
    },
    {
        "description": "Кошка и собака",
        "image": "cat and dog.jpg"
    }
]

print(data)


def search(dic, word):
    """Поиск в словаре по слову"""
    new_list = []
    for item in dic:
        if word in item["description"].split(' '):
            new_list.append(item)
    if new_list:
        return new_list
    else:
        return ["Ничего не найдено"]


print(search(data, "sdfsd"))
