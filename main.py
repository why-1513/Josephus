from Josephus_deque import *
import time
from CreateInfoFile import *
from TxtReader import *
from ZipReader import *
from CsvReader import *


def wait_for_input_int(prompt, check_func, error_prompt):
    while True:
        value = input(prompt)
        try:
            value = int(value)
            if check_func(value):
                raise ValueError
            break
        except ValueError:
            print(error_prompt)
    return value


def start_get_input():
    # total_num = wait_for_input_int(prompt="请输入总人数：", check_func=lambda x: x < 0, error_prompt="非法输入，请输入大于零的数")
    _step_num = wait_for_input_int(prompt="请输入循环的数：", check_func=lambda x: x < 0, error_prompt="非法输入，请输入大于零的数")
    _start_pos = wait_for_input_int(prompt="请输入开始的位置：", check_func=lambda x: x < 0, error_prompt="非法输入，请输入大于等于零的数")
    return _step_num, _start_pos


if __name__ == '__main__':
    step_num, start_pos = start_get_input()
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


