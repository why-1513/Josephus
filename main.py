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
    # create_info_txt(total_num)
    # file = TxtReader('info1.txt')

    # file = CsvReader('info.csv')

    file = ZipReader('info.zip')
    # file.list_files()

    josephus = file.read_person_info(step_num, start_pos)

    for person in josephus:
        pass
    josephus.josephus_print()



