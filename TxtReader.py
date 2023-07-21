from Josephus_deque import Person, Josephus
from FileReader import Reader


class TxtReader(Reader):

    def __init__(self, filename=''):
        if not filename.endswith('.txt'):
            raise ValueError(f"Invalid file type, '{filename}' is not a txt file")
        self.filename = filename

    def read_person_info(self, step_num, start_pos):
        person_info = Josephus(step_num, start_pos)
        try:
            with open(self.filename, 'r') as f:
                lines = f.readlines()
            for line in lines:
                # parse person info from line
                name, gender, age = line.strip().split(':')
                if gender not in ['男', '女']:
                    raise ValueError(f"Invalid gender '{gender}' on line '{line.strip()}' in file '{self.filename}'")
                try:
                    age = int(age)
                except ValueError:
                    raise ValueError(f"Invalid age '{age}' on line '{line.strip()}' in file '{self.filename}'")
                person = Person(name, gender, age)
                person_info.add_one_person(person)
        except FileNotFoundError:
            raise FileNotFoundError(f"File '{self.filename}' not found")

        return person_info
