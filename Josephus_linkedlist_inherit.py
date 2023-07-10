class Person:
    def __init__(self, value, name):
        self.value = value
        self.next = None
        self.name = name


class JosephusLinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def add_person(self, value, name):
        new_person = Person(value, name)
        if not self.head:
            self.head = new_person
            new_person.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next

            temp.next = new_person
            new_person.next = self.head

        self.length += 1

    def delete_person(self, value):
        if not self.head:
            print("链表为空，不能删除节点。")
            return
        if self.head.value == value:
            if self.head == self.head.next:
                self.head = None
            else:
                temp = self.head
                while temp.next != self.head:
                    temp = temp.next
                temp.next = self.head.next
                self.head = self.head.next
                self.length -= 1
            return

        temp = self.head
        while temp.next != self.head and temp.next.value != value:
            temp = temp.next

        if temp.next == self.head:
            print("没有找到要删除的节点。")
        else:
            temp.next = temp.next.next
            self.length -= 1

    def display(self):
        if not self.head:
            print("链表为空。")
            return
        temp = self.head
        while True:
            print(temp.value)
            temp = temp.next
            if temp == self.head:
                break
        print()


class Josephus(JosephusLinkedList):
    def __init__(self, step_num):
        super().__init__()
        self.step = step_num
        self.out_list = []
        self.survivor_value = None
        self.survivor_name = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.head is None:
            raise StopIteration

        if self.length == 1:
            value = self.head.value
            name = self.head.name
            self.delete_person(self.head.value)
            self.survivor_value = value
            self.survivor_name = name
            return value

        temp = self.head

        for i in range(self.step - 1):
            temp = temp.next

        value = temp.value
        name = temp.name
        self.delete_person(value)
        self.out_list.append([value, name])
        self.head = temp.next
        return value

    def josephus_print(self):
        print('出局顺序：{}'.format(self.out_list))
        print('幸存者:{},{}'.format(self.survivor_value, self.survivor_name))
