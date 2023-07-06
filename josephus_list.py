def josephus_list(num, step):
    people = list(range(1, num+1))
    people_out = []
    inc_count = 0
    while len(people) > 1:
        temp = people.pop(0)
        inc_count += 1
        if inc_count == step:
            inc_count = 0
            people_out.append(temp)
            continue
        people.append(temp)
    print('出局顺序：{}'.format(people_out))
    print('最后生还者{}：'.format(people[0]))


def josephus_list_input():
    total_num = int(input("请输入总人数："))
    step_num = int(input("请输入循环的数："))
    return total_num, step_num
