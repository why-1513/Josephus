from Josephus_deque import *
import time
from CreateInfoFile import *
from FileReader import *


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
    step_num = wait_for_input_int(prompt="请输入淘汰的数：", check_func=lambda x: x < 0, error_prompt="非法输入，请输入大于零的数")
    start_pos = wait_for_input_int(prompt="请输入开始的位置：", check_func=lambda x: x < 0, error_prompt="非法输入，请输入大于等于零的数")

    # create_info_json(total_num)
    # file = FileReader('info.json')
    # info_list = file.json_read()

    # create_info_txt(total_num)
    file = FileReader('info.txt')
    info_list = file.txt_read()

    josephus = Josephus(step_num, start_pos)
    total_num = len(info_list)

    for info in info_list:
        josephus.add_person(Person(info['name'], info['gender'], info['age']))

    for person in josephus:
        pass
    josephus.josephus_print()

