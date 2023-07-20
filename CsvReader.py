import csv
from TxtReader import Reader


class CsvReader(Reader):
    def __init__(self, filename=''):
        if not filename.endswith('.csv'):
            raise ValueError(f"Invalid file type, '{filename}' is not a csv file")
        self.filename = filename

    def read_all_person(self):
        person_infos = []
        try:
            with open(self.filename, 'r', newline='') as csvfile:
                # 每一行都被解析为一个字典，其中字典的键是CSV文件的表头，值是该行的值。
                reader = csv.DictReader(csvfile)
                for row in reader:
                    name = row['name']
                    gender = row['gender']
                    try:
                        age = int(row['age'])
                    except ValueError:
                        raise ValueError(f"Invalid age '{row['age']}' in file '{self.filename}'")
                    if gender not in ['男', '女']:
                        raise ValueError(f"Invalid gender '{gender}' in file '{self.filename}'")
                    info_dict = {
                        'name': name,
                        'gender': gender,
                        'age': age
                    }
                    person_infos.append(info_dict)

        except FileNotFoundError:
            raise FileNotFoundError(f"File '{self.filename}' not found")

        return person_infos

