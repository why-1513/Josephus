from faker import Faker


class Person:
    def __init__(self, value, name):
        self.value = value
        self.next = None
        self.name = name


def create_circular_linked_list(total_num):
    fk = Faker(locale="zh-CN")
    name_list = []
    for i in range(total_num):
        name_list.append(fk.name())

    print(name_list)
    head = Person(1, name_list[0])
    node_current = head
    for i in range(2, total_num + 1):
        node_new = Person(i, name_list[i-1])
        node_current.next = node_new
        node_current = node_new

    node_current.next = head
    return head


class Josephus_ring:
    def __init__(self):
        self.head = None
        self.total_num = int(input("请输入总人数："))
        self.step_num = int(input("请输入循环的数："))

    def josephus_ring_running(self):
        if self.total_num < 1 or self.step_num < 1:
            return None
        self.head = create_circular_linked_list(self.total_num)
        out_list = []
        # 定位到最后一个节点
        prev = self.head
        while prev.next != self.head:
            prev = prev.next

        while self.head != self.head.next:
            for _ in range(self.step_num-1):
                prev = self.head
                self.head = self.head.next
            prev.next = self.head.next
            out_list.append([self.head.value, self.head.name])
            self.head = self.head.next
        print('出局者顺序：{}'.format(out_list))
        print('幸存者序号:{}；幸存者姓名：{}'.format(self.head.value, self.head.name))








