from josephus_list import *
import time


if __name__ == '__main__':
    start_time = time.time()
    total_num, step_num = josephus_list_input()
    josephus_list(total_num, step_num)
    end_time = time.time()
    print(end_time - start_time)