import json
import logging


def load_posts():
    """Загружает список из файла"""

    with open("posts.json", 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def get_posts_by_combination_simbols(combination_simbols):
    """Возвращает пост по введенной комбинации символов"""
    data = load_posts()
    result = []

    for post in data:
        if combination_simbols.lower() in post["content"].lower():
            result.append(post)

    return result


def save_picture(picture):
    """Сохраняет изображение"""
    filename = picture.filename

# путь по которому можно работать с картинкой
    picture.save(f'./uploads/{filename}')
    return f'uploads/{filename}'


def add_post(post):
    """Возвращает добавленный пост, предварительно добавив его в файл json"""
    data_posts = load_posts()
    data_posts.append(post)

    with open("posts.json", 'w', encoding='utf-8') as file:
        json.dump(data_posts, file)
    return post


