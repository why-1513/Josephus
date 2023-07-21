import zipfile
from TxtReader import TxtReader
from CsvReader import CsvReader
from Josephus_deque import Josephus
from FileReader import Reader


class ZipReader(Reader):

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

    def read_person_info(self, step_num, start_pos, file_name=None):
        if file_name is None:
            file_names = self.list_files()
        else:
            if file_name not in self.list_files():
                raise ValueError(f"File '{file_name}' not found in zip file '{self.filename}'")
            file_names = [file_name]

        person_info = Josephus(step_num, start_pos)
        for file_name in file_names:
            try:
                if file_name.endswith('.txt'):
                    reader = TxtReader(file_name)
                elif file_name.endswith('.csv'):
                    reader = CsvReader(file_name)
                persons = reader.read_person_info(step_num, start_pos)
                for person in persons:
                    person_info.add_one_person(person)
            except KeyError:
                raise KeyError(f"File '{file_name}' not found in zip file '{self.filename}'")
            except zipfile.BadZipFile:
                raise zipfile.BadZipFile(f"Invalid zip file '{self.filename}'")
        print(len(person_info))
        return person_info
