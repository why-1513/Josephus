from josephus_list import *
from josephus_linked_list import *
from Josephus_linkedlist_inherit import *
import time
from faker import Faker


if __name__ == '__main__':
    josephus = Josephus(3)
    for i in range(1, 9):
        josephus.add_person(i)

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
