import json
import random
import itertools
from faker import Faker
from conf import MODEL
fake = Faker()


def main() -> json:
    """
    Функция запускает генератор, который возвращает словари (по умолчанию задается формирование 100 словарей).
    Запись списка книг происходит в json.
    """

    first_g = gen_function(100)
    new_list = list(first_g)
    with open('books_dict_json.txt', 'w', encoding='utf-8') as result_file:
        json.dump(new_list, result_file, indent=4, ensure_ascii=False)


def gen_function(how_many_dict: int, pk=1) -> dict:
    for i in range(how_many_dict):
        result = {}
        result['model'] = MODEL
        result['pk'] = i+1
        result['title'] = get_title()
        result['year'] = get_year()
        result['pages'] = get_pages()
        result['isbn13'] = get_isbn()
        result['rating'] = get_rating()
        result['price'] = get_price()
        result['author'] = get_author()
        yield result


def get_title() -> str:
    with open('books.txt', 'r', encoding="utf-8") as f:
        all_titles = f.readlines()
        title = random.choice(all_titles)
        return title


def get_year() -> int:
    return random.randint(1997, 2008)


def get_pages() -> int:
    return random.randint(1, 1000)


def get_isbn() -> str:
    Faker.seed(0)
    return fake.isbn13()


def get_rating() -> float:
    return round(random.uniform(0, 5), 2)


def get_price() -> float:
    return random.uniform(100, 5000)


def get_author() -> list:
    Faker.seed(0)
    return list(fake.unique.name() for _ in range(random.randint(1, 3)))


if __name__ == '__main__':
    main()
