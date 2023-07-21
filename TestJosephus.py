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
        self.josephus = Josephus(3, 0)
        file0 = TxtReader('info1.txt')
        josephus = file0.read_person_info(3, 0)
        self.assertEqual(len(josephus), 8)

    def test_read_person_info_from_csv(self):
        self.josephus = Josephus(3, 0)
        file1 = CsvReader('info.csv')
        josephus = file1.read_person_info(3, 0)
        self.assertEqual(len(josephus), 18)

    def test_read_person_info_from_zip(self):
        self.josephus = Josephus(3, 0)
        file2 = ZipReader('info.zip')
        josephus = file2.read_person_info(3, 0)
        self.assertEqual(len(josephus), 36)

    def test_josephus_txt(self):
        step_num, start_pos = [3, 0]
        file_txt = TxtReader('info1.txt')

        josephus = file_txt.read_person_info(step_num, start_pos)

        for person in josephus:
            pass
        self.assertEqual(josephus.survivor.name, '姜莹')

    def test_josephus_csv(self):
        step_num, start_pos = [4, 1]
        file_csv = CsvReader('info.csv')

        josephus = file_csv.read_person_info(step_num, start_pos)

        for person in josephus:
            pass
        self.assertEqual(josephus.survivor.name, '袁敏')

    def test_josephus_zip(self):
        step_num, start_pos = [5, 2]
        file_zip = ZipReader('info.zip')

        josephus = file_zip.read_person_info(step_num, start_pos)

        for person in josephus:
            pass
        self.assertEqual(josephus.survivor.name, '何秀华')


