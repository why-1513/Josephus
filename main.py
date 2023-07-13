from Josephus_list import *
from Josephus_linked_list import *
from Josephus_linkedlist_inherit import *
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

    total_num = wait_for_input_int(prompt="请输入总人数：", check_func=lambda x: x < 0, error_prompt="非法输入，请输入大于零的数")
    step_num = wait_for_input_int(prompt="请输入淘汰的数：", check_func=lambda x: x < 0, error_prompt="非法输入，请输入大于零的数")

    # create_info_json(total_num)
    # file = FileReader('info.json')
    # info_list = file.json_read()

    # create_info_txt(total_num)
    # file = FileReader('info.txt')
    # info_list = file.txt_read()

    josephus = Josephus(step_num)

    for i in range(1, total_num + 1):
        josephus.add_person(i, info_list[i-1]["name"], info_list[i-1]["gender"], info_list[i-1]["age"])

    for person in josephus:
        print(person)
    josephus.josephus_print()

