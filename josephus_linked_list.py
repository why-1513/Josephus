class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def create_circular_linked_list(total_num):
    head = Node(1)
    node_current = head
    for i in range(2, total_num + 1):
        node_new = Node(i)
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
            out_list.append(self.head.value)
            self.head = self.head.next
        print('出局顺序：{}'.format(out_list))
        print('最后生还者:{}'.format(self.head.value))








