from Josephus_deque import Josephus
from TxtReader import TxtReader
from ZipReader import ZipReader
from CsvReader import CsvReader
from Log import Logger, start_get_input


if __name__ == '__main__':
    logger = Logger('MyLogger', log_file='test.log')
    step_num, start_pos = start_get_input(logger)
    # create_info_txt(total_num)
    file = TxtReader('info1.txt')

    # file = ZipReader('info.zip')
    # file.list_files()

    # csv_reader = CsvReader('info.csv')

    josephus = file.read_person_info(step_num, start_pos)

    for person in josephus:
        pass
    josephus.josephus_print()



