from josephus_list import *
import time


if __name__ == '__main__':
    total_num, step_num = josephus_list_input()
    start_time = time.perf_counter()
    josephus_list(total_num, step_num)
    end_time = time.perf_counter()
    run_time = end_time-start_time
    print('josephus_list运行时间:{}'.format(run_time))
