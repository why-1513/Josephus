import csv
from Josephus_deque import Person
from FileReader import Reader


class CsvReader(Reader):

    def __init__(self, filename=''):
        if not filename.endswith('.csv'):
            raise ValueError(f"Invalid file type, '{filename}' is not a csv file")
        self.filename = filename
        self.persons = []

    def read_person_info(self):
        try:
            with open(self.filename, 'r', newline='') as csvfile:
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
                    person = Person(name, gender, age)
                    self.persons.append(person)
        except FileNotFoundError:
            raise FileNotFoundError(f"File '{self.filename}' not found")
