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


if __name__ == '__main__':

    # total_num = wait_for_input_int(prompt="请输入总人数：", check_func=lambda x: x < 0, error_prompt="非法输入，请输入大于零的数")
    step_num = wait_for_input_int(prompt="请输入循环的数：", check_func=lambda x: x < 0, error_prompt="非法输入，请输入大于零的数")
    start_pos = wait_for_input_int(prompt="请输入开始的位置：", check_func=lambda x: x < 0, error_prompt="非法输入，请输入大于等于零的数")

    # create_info_txt(total_num)
    file = TxtReader('info1.txt')
    info_list = file.read_file()

    # file = ZipReader('info.zip')
    # file.list_files()
    # info_list = file.read_zip()

    # csv_reader = CsvReader('info.csv')
    # info_list = csv_reader.read_csv()

    josephus = Josephus(step_num, start_pos)
    total_num = len(info_list)

    for info in info_list:
        josephus.add_person(Person(info['name'], info['gender'], info['age']))

    for person in josephus:
        pass
    josephus.josephus_print()

