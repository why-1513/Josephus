import unittest
from Josephus_deque import Person, Josephus
from TxtReader import TxtReader
from ZipReader import ZipReader
from CsvReader import CsvReader


class TestJosephus(unittest.TestCase):
    def setUp(self):
        self.josephus = None

    def test_add_one_person(self):
        self.josephus = Josephus(3, 0)
        p = Person('Alice', '女', 25)
        self.josephus.add_one_person(p)
        self.assertIn(p, self.josephus)

    def test_delete_person(self):
        self.josephus = Josephus(3, 0)
        p1 = Person('Alice', '女', 25)
        p2 = Person('Bob', '男', 30)
        p3 = Person('Charlie', '男', 35)
        p4 = Person('Dave', '男', 40)
        self.josephus.add_one_person(p1)
        self.josephus.add_one_person(p2)
        self.josephus.add_one_person(p3)
        self.josephus.add_one_person(p4)
        out_person = self.josephus.delete_person()
        self.assertEqual(out_person, p3)
        out_person = self.josephus.delete_person()
        self.assertEqual(out_person, p2)

    def test_read_person_info_from_txt(self):
        step_num, start_pos = [3, 0]
        reader = TxtReader('info1.txt')

        josephus = Josephus(step_num, start_pos)
        josephus.add_persons(reader)
        self.assertEqual(len(josephus), 8)

    def test_read_person_info_from_csv(self):
        step_num, start_pos = [4, 1]
        reader = CsvReader('info.csv')

        josephus = Josephus(step_num, start_pos)
        josephus.add_persons(reader)
        self.assertEqual(len(josephus), 18)

    def test_read_person_info_from_zip(self):
        step_num, start_pos = [5, 2]
        reader = ZipReader('info.zip')

        josephus = Josephus(step_num, start_pos)
        josephus.add_persons(reader)
        self.assertEqual(len(josephus), 36)

    def test_josephus_txt(self):
        step_num, start_pos = [3, 0]
        reader = TxtReader('info1.txt')

        josephus = Josephus(step_num, start_pos)
        josephus.add_persons(reader)

        for person in josephus:
            pass
        self.assertEqual(josephus.survivor.name, '姜莹')

    def test_josephus_csv(self):
        step_num, start_pos = [4, 1]
        reader = CsvReader('info.csv')

        josephus = Josephus(step_num, start_pos)
        josephus.add_persons(reader)

        for person in josephus:
            pass
        self.assertEqual(josephus.survivor.name, '袁敏')

    def test_josephus_zip(self):
        step_num, start_pos = [5, 2]
        reader = ZipReader('info.zip')

        josephus = Josephus(step_num, start_pos)
        josephus.add_persons(reader)

        for person in josephus:
            pass
        self.assertEqual(josephus.survivor.name, '李凤英')


