import logging


def wait_for_input_int(prompt, check_func, error_prompt):
    while True:
        value = input(prompt)
        try:
            value = int(value)
            if check_func(value):
                raise ValueError
            break
        except ValueError:
            logging.error(error_prompt)
            print(error_prompt)
    return value


def start_get_input():
    logging.info('开始获取用户输入')
    _step_num = wait_for_input_int(prompt="请输入循环的数：",
                                   check_func=lambda x: x < 0, error_prompt="非法输入，请输入大于零的数")
    _start_pos = wait_for_input_int(prompt="请输入开始的位置：",
                                    check_func=lambda x: x < 0, error_prompt="非法输入，请输入大于等于零的数")
    logging.info('获取用户输入结束')
    return _step_num, _start_pos

