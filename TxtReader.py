
class TxtReader:

    def __init__(self, filename=''):
        if not filename.endswith('.txt'):
            raise ValueError(f"Invalid file type, '{filename}' is not a txt file")
        self.filename = filename

    def read_file(self):
        person_infos = []
        try:
            with open(self.filename, 'r') as f:
                lines = f.readlines()
            for line in lines:
                # 使用strip方法去除字符串两端的空白字符，使用split方法将每一行的信息按照'，'进行分隔 ['程凤兰':'女':'47']
                info = line.strip().split(':')
                if len(info) == 3:
                    name, gender, age = info
                    try:
                        age = int(age)
                    except ValueError:
                        raise ValueError(f"Invalid age '{age}' on line '{line.strip()}' in file '{self.filename}'")

                    if gender not in ['男', '女']:
                        raise ValueError(f"Invalid gender '{gender}' on line '{line.strip()}' in file '{self.filename}'")
                    info_dict = {
                        'name': name,
                        'gender': gender,
                        'age': age
                    }
                    person_infos.append(info_dict)
                else:
                    raise ValueError(f"Invalid line '{line.strip()}' in file '{self.filename}'")

        except FileNotFoundError:
            raise FileNotFoundError(f"File '{self.filename}' not found")

        return person_infos
