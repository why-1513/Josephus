import json


def json_read(json_filename=''):
    with open(json_filename, 'r') as f:
        data = []
        for line in f:
            obj = json.loads(line.strip())
            data.append(obj)

    f.close()

    return data

