import json


def task():
    filename = "input.json"
    with open(filename) as i:
        json_obj = json.load(i)
    # TODO считать содержимое JSON файла

    return max(json_obj, key=lambda item: item["score"])  # TODO найти максимальный элемент по ключу score


if __name__ == "__main__":
    print(task())
