import json
import re

BOOKS_FILE = "books.md"
BOOK_REGEX = r"(?P<position>(?<=#\s)\d{1,2})\.\s\[(?P<book>.+?)\]\(" \
               r"(?P<book_url>(https://.+?))\)\sby\s+(?P<author>([\w\.\&\s\']+))" \
               r"\((?P<recommended>(\d{1,2}\.\d{1,2}\%))\srecommended\)\s" \
               r"\!\[\]\((?P<cover_url>(https://.+?))\)\s+" \
               r"\"(?P<description>.+?)\""

def task():
    book_pattern = re.compile(BOOK_REGEX, re.DOTALL)  # флаг re.DOTALL описывает, что под символом точка может содержаться символ переноса строки

    with open(BOOKS_FILE) as f:
        for book in book_pattern.finditer(f.read()):
            print(json.dumps(book.groupdict(), indent=4))


if __name__ == '__main__':
    task()
