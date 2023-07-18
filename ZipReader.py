import zipfile


class ZipReader:
    def __init__(self, filename=''):
        self.filename = filename

    def list_files(self):
        try:
            with zipfile.ZipFile(self.filename, 'r') as myzip:
                return myzip.namelist()
        except zipfile.BadZipFile:
            raise zipfile.BadZipFile(f"Invalid zip file '{self.filename}'")
        except FileNotFoundError:
            raise FileNotFoundError(f"File '{self.filename}' not found")

    def read_zip(self, file_name=None):  # 默认打开zip下全部文件，指定文件打开时，打开指定文件
        if file_name is None:
            file_names = self.list_files()
        else:
            if file_name not in self.list_files():
                raise ValueError(f"File '{file_name}' not found in zip file '{self.filename}'")
            file_names = [file_name]

        person_infos = []
        for file_name in file_names:
            try:
                with zipfile.ZipFile(self.filename, 'r') as myzip:
                    with myzip.open(file_name) as f:
                        lines = f.readlines()
                for line in lines:
                    info = line.decode('gbk').strip().split(':')
                    if len(info) == 3:
                        name, gender, age = info
                        try:
                            age = int(age)
                        except ValueError:
                            raise ValueError(f"Invalid age '{age}' on line '{line.strip()}' in file '{file_name}'")

                        if gender not in ['男', '女']:
                            raise ValueError(f"Invalid gender '{gender}' on line '{line.strip()}' in file '{file_name}'")
                        info_dict = {
                            'name': name,
                            'gender': gender,
                            'age': age
                        }
                        person_infos.append(info_dict)
                    else:
                        raise ValueError(f"Invalid line '{line.strip()}' in file '{file_name}'")

            except KeyError:
                raise KeyError(f"File '{file_name}' not found in zip file '{self.filename}'")

            except zipfile.BadZipFile:
                raise zipfile.BadZipFile(f"Invalid zip file '{self.filename}'")

        return person_infos


