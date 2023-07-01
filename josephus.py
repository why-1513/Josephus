def josephus(n, k):
    people = list(range(1, n+1))
    people_out = []
    i = 0
    while len(people) > 1:
        temp = people.pop(0)
        i = i+1
        if i == k:
            i = 0
            people_out.append(temp)
            continue
        people.append(temp)
    print('出局顺序：{}'.format(people_out))
    print('最后生还者{}：'.format(people[0]))

n = int(input("请输入总人数："))
k = int(input("请输入循环的数："))
josephus(n, k)
