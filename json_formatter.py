import json
import sys


def flatten_json(json_obj, path=""):
    """
    Flatten a JSON object into a list of strings.

    :param json_obj: The name of foo
    :param path: The path to the JSON object (used when dealing with objects nested inside other objects)
    :return: returns a list of strings where each entry corresponds to a JSON entry for each terminal value with its
     flattened path.
    """
    entry_list = []

    for key, value in json_obj.items():
        if type(value) is dict:
            entry_list += flatten_json(value, f'{path}{key}.')
        else:
            entry_list.append(f'"{path}{key}": {json.dumps(value)}')

    return entry_list


if __name__ == '__main__':
    flattened_obj = flatten_json(json.load(sys.stdin))

    if len(flattened_obj) == 0:
        print("{}")
        sys.exit()

    print("{")
    last_entry = flattened_obj.pop()
    for entry in flattened_obj:
        print(f'    {entry},')
    print(f'    {last_entry}')
    print("}")
