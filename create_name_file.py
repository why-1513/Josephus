from faker import Faker
import json


def create_name_json(total_num):
    # fk = Faker(locale="zh-CN")
    fk = Faker()
    name_list = []
    for i in range(total_num):
        name = {
            'name': fk.name()
        }
        name_list.append(name)
        with open('names.json', 'w') as f:
            json.dump(name_list, f)

    f.close()
