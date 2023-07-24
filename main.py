from Josephus_deque import Josephus
from TxtReader import TxtReader
from ZipReader import ZipReader
from CsvReader import CsvReader
from GetInput import start_get_input
import logging


if __name__ == '__main__':
    # Configure logging to save messages to a file
    logging.basicConfig(filename='test.log', filemode='w',
                        format='%(asctime)s [%(levelname)s] %(message)s', level=logging.INFO)
    step_num, start_pos = start_get_input()
    # reader = TxtReader('info1.txt')
    # reader = CsvReader('info.csv')
    reader = ZipReader('info.zip')

    josephus = Josephus(step_num, start_pos)
    josephus.add_persons(reader)

    for person in josephus:
        pass
    josephus.josephus_print()



