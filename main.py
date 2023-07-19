from Josephus_deque import *
import time
from CreateInfoFile import *
from TxtReader import *
from ZipReader import *
from CsvReader import *
from Log import *


if __name__ == '__main__':
    logger = Logger('MyLogger', log_file='test.log')
    step_num, start_pos = start_get_input(logger)
    # create_info_txt(total_num)
    file = TxtReader('info1.txt')
    info_list = file.read_txt()

    # file = ZipReader('info.zip')
    # file.list_files()
    # info_list = file.read_zip()

    # csv_reader = CsvReader('info.csv')
    # info_list = csv_reader.read_csv()
    total_num = len(info_list)

    josephus = Josephus(step_num, start_pos)
    josephus.add_person(info_list)

    for person in josephus:
        pass
    josephus.josephus_print()



