from josephus_list import *
from josephus_linked_list import *
from Josephus_linkedlist_inherit import *
import time
from create_name_file import create_name_json
from File_read import json_read


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

    create_name_json(total_num)  # 创建姓名文件
    info = json_read('names.json')

    josephus = Josephus(step_num)

    for i in range(1, total_num + 1):
        josephus.add_person(i, info[0][i-1]["name"])

    for person in josephus:
        print(person)
    josephus.josephus_print()
    # 测试josephus_list
    """
    total_num, step_num = josephus_list_input()
    start_time = time.perf_counter()
    josephus_list(total_num, step_num)
    end_time = time.perf_counter()
    run_time = end_time-start_time
    print('josephus_list运行时间:{}'.format(run_time))
    """
    """
    # 测试josephus_linked_list
    josephus_ring_ = Josephus_ring()
    start_time = time.perf_counter()
    josephus_ring_.josephus_ring_running()
    end_time = time.perf_counter()
    run_time = end_time - start_time
    print('josephus_linked_list运行时间:{}'.format(run_time))
    """
