import json


def task():
    filename = "input.json"
    with open(filename) as i:
        json_obj = json.load(i)

    gen_exr = (item["contains_improvement_appeals"] for item in json_obj)
    return sum(gen_exr)


if __name__ == "__main__":
    print(task())
