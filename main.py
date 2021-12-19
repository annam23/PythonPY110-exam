import json
import random
import itertools
from faker import Faker
from conf import MODEL


def main():
    first_g = gen_function()
    new_list = []
    for _ in range(100):
        new_list.append(next(first_g))
        print(new_list)
        with open('books_dict_json.txt', 'w', encoding='utf-8') as result_file:
            json.dump(new_list, result_file, indent=4, ensure_ascii = False)


def gen_function(pk=1) -> dict:
    result = {}
    result['model'] = MODEL
    for i in itertools.count(pk,1):
        result['pk'] = i
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
    year = random.randint(1997, 2008)
    return year


def get_pages() -> int:
    pages = random.randint(1, 1000)
    return pages


def get_isbn() -> str:
    fake = Faker()
    Faker.seed(0)
    isbn = fake.unique.isbn13()
    return isbn


def get_rating() -> float:
    rating = random.uniform(0, 5)
    return rating


def get_price() -> float:
    price = random.uniform(100, 5000)
    return price


def get_author() -> list:
    fake = Faker()
    Faker.seed(0)
    names = list(fake.unique.name() for _ in range(random.randint(1, 3)))
    return names


if __name__ == '__main__':
    main()
