from faker import Faker
import json
import random


def create_name_json(total_num):
    fk = Faker("zh_CN")
    person_info = []
    for i in range(total_num):
        info = {
            'name': fk.name(),
            'gender': random.choice(['男', '女']),
            'age': random.randint(18, 60)

        }
        person_info.append(info)
    with open('info.json', 'w') as f:
        json.dump(person_info, f)

    f.close()


