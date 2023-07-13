import json


def json_read(json_filename=''):

    with open(json_filename, 'r') as f:
        person_info = json.load(f)
    f.close()

    return person_info

