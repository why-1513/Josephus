from Josephus_deque import Josephus
from TxtReader import TxtReader
from ZipReader import ZipReader
from CsvReader import CsvReader
from Log import Logger


if __name__ == '__main__':
    logger = Logger('MyLogger', log_file='test.log')
    step_num, start_pos = start_get_input(logger)
    # create_info_txt(total_num)
    # file = TxtReader('info1.txt')

    file = ZipReader('info.zip')
    file.list_files()

    # csv_reader = CsvReader('info.csv')

    info_list = file.read_all_person()
    total_num = len(info_list)

    josephus = Josephus(step_num, start_pos)
    josephus.add_person(info_list)

    for person in josephus:
        pass
    josephus.josephus_print()



