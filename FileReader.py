import json


class FileReader:

    def __init__(self, filename=''):
        self.filename = filename

    def json_read(self):
        try:
            with open(self.filename, 'r') as f:
                person_infos = json.load(f)
        except FileNotFoundError:
            print("File not found: {}".format(self.filename))
            return []

        except json.decoder.JSONDecodeError:
            print("JSON decode error: {}".format(self.filename))
            return []

        return person_infos

    def txt_read(self):
        person_infos = []
        try:
            with open(self.filename, 'r') as f:
                lines = f.readlines()
            for line in lines:
                # 使用strip方法去除字符串两端的空白字符，使用split方法将每一行的信息按照'，'进行分隔 ['姓名：程凤兰', '性别：女', '年龄：47']
                parts = line.strip().split('，')
                # [3:]表示从字符串的第四个字符开始
                info = {
                    'name': parts[0][3:],
                    'gender': parts[1][3:],
                    'age': int(parts[2][3:])
                }
                person_infos.append(info)
        except FileNotFoundError:
            print("File not found: {}".format(self.filename))
            return []
        except IOError:
            print("Error reading file: {}".format(self.filename))
            return []
        return person_infos
