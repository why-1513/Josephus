class Person:
    def __init__(self, value, name, gender, age):
        self.value = value
        self.next = None
        self.name = name
        self.gender = gender
        self.age = age


class JosephusLinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def add_person(self, value, name, gender, age):
        new_person = Person(value, name, gender, age)
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


class Josephus(JosephusLinkedList):
    def __init__(self, step_num):
        super().__init__()
        self.step = step_num
        self.out_list = []
        self.survivor = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.head is None:
            raise StopIteration

        if self.length == 1:
            self.survivor = self.head
            self.delete_person(self.survivor.value)
            return self.survivor

        temp = self.head

        for i in range(self.step - 1):
            temp = temp.next

        out_person = temp
        self.out_list.append(out_person)
        self.delete_person(out_person.value)

        self.head = temp.next

        return out_person

    def josephus_print(self):
        print('出局者顺序:')
        for i in range(len(self.out_list)):
            print('编号：{} 姓名:{} 性别：{} 年龄：{}'.format(
                self.out_list[i].value, self.out_list[i].name, self.out_list[i].gender, self.out_list[i].age))
        print('幸存者：')
        print('编号：{} 姓名:{} 性别：{} 年龄：{}'.format(
            self.survivor.value, self.survivor.name, self.survivor.gender, self.survivor.age))
