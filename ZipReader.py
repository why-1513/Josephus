import zipfile
from TxtReader import TxtReader
from CsvReader import CsvReader
from FileReader import Reader


class ZipReader(Reader):

    def __init__(self, filename=''):
        self.filename = filename
        self.file = zipfile.ZipFile(self.filename, 'r')
        self.persons = []

    def list_files(self):
        try:
            return self.file.namelist()
        except zipfile.BadZipFile:
            raise zipfile.BadZipFile(f"Invalid zip file '{self.filename}'")
        except FileNotFoundError:
            raise FileNotFoundError(f"File '{self.filename}' not found")

    def read_person_info(self, file_name=None):
        if file_name is None:
            file_names = self.list_files()
        else:
            if file_name not in self.list_files():
                raise ValueError(f"File '{file_name}' not found in zip file '{self.filename}'")
            file_names = [file_name]

        for file_name in file_names:
            try:
                if file_name.endswith('.txt'):
                    reader = TxtReader(file_name)
                elif file_name.endswith('.csv'):
                    reader = CsvReader(file_name)
                reader.read_person_info()
                self.persons.extend(reader.persons)
            except KeyError:
                raise KeyError(f"File '{file_name}' not found in zip file '{self.filename}'")
            except zipfile.BadZipFile:
                raise zipfile.BadZipFile(f"Invalid zip file '{self.filename}'")
