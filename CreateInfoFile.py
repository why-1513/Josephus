from faker import Faker
import json
import random


def create_info_json(total_num):
    person_infos = []
    for i in range(total_num):
        info = {
            'name': Faker("zh_CN").name(),
            'gender': random.choice(['男', '女']),
            'age': random.randint(18, 60)
        }
        person_infos.append(info)
    with open('info.json', 'w') as f:
        json.dump(person_infos, f)


def create_info_txt(total_num):
    person_infos = []
    for i in range(total_num):
        info = {
            'name': Faker("zh_CN").name(),
            'gender': random.choice(['男', '女']),
            'age': random.randint(18, 60)
        }
        person_infos.append(info)
    print(person_infos)
    f = open('info.txt', 'w')
    for person in person_infos:
        f.write(f"{person['name']}:{person['gender']}:{person['age']}\n")
    f.close()

