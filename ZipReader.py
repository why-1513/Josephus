import zipfile
from TxtReader import TxtReader
from CsvReader import CsvReader


class Reader:

    def read_all_person(self):
        raise NotImplementedError()


class ZipReader:
    def __init__(self, filename=''):
        self.filename = filename
        self.file = zipfile.ZipFile(self.filename, 'r')

    def list_files(self):
        try:
            return self.file.namelist()
        except zipfile.BadZipFile:
            raise zipfile.BadZipFile(f"Invalid zip file '{self.filename}'")
        except FileNotFoundError:
            raise FileNotFoundError(f"File '{self.filename}' not found")

    def read_all_person(self, file_name=None):  # 默认打开zip下全部文件，指定文件打开时，打开指定文件
        if file_name is None:
            file_names = self.list_files()
        else:
            if file_name not in self.list_files():
                raise ValueError(f"File '{file_name}' not found in zip file '{self.filename}'")
            file_names = [file_name]

        person_infos = []
        for file_name in file_names:
            try:
                if file_name.endswith('.txt'):
                    reader = TxtReader(file_name)
                elif file_name.endswith('.csv'):
                    reader = CsvReader(file_name)
                person_infos = reader.read_all_person()

            except KeyError:
                raise KeyError(f"File '{file_name}' not found in zip file '{self.filename}'")

            except zipfile.BadZipFile:
                raise zipfile.BadZipFile(f"Invalid zip file '{self.filename}'")

        return person_infos




