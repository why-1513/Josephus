import json
import logging


class FileReader:

    def __init__(self, filename=''):
        self.filename = filename

    def json_read(self):
        try:
            with open(self.filename, 'r') as f:
                person_infos = json.load(f)
        except FileNotFoundError:
            logging.log(logging.ERROR, "File not found: {}".format(self.filename))
            logging.error("File not found: {}".format(self.filename))
            raise ("File not found: {}".format(self.filename))

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
                # 使用strip方法去除字符串两端的空白字符，使用split方法将每一行的信息按照'，'进行分隔 ['程凤兰', '女', '47']
                parts = line.strip().split(':')
                info = {
                    'name': parts[0],
                    'gender': parts[1],
                    'age': int(parts[2])
                }
                person_infos.append(info)
        except FileNotFoundError:
            print("File not found: {}".format(self.filename))
            return []
        except IOError:
            print("Error reading file: {}".format(self.filename))
            return []
        return person_infos
