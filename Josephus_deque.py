from collections import deque


class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age


class Josephus(deque):
    def __init__(self, step_num, start_pos):
        super().__init__()
        self.step = step_num
        self.out_list = []
        self.start_pos = start_pos

    def add_person(self, new_person):
        self.append(new_person)

    def __iter__(self):
        return self

    def __next__(self):
        if len(self) == 1:
            self.survivor = self.pop()
            raise StopIteration

        if self.start_pos is not None:
            # 旋转到指定位置
            self.rotate(-self.start_pos)
            self.start_pos = None

        self.rotate(-self.step)
        out_person = self.pop()
        self.out_list.append(out_person)

        return out_person

    def josephus_print(self):
        print('出局者顺序:')
        for i in range(len(self.out_list)):
            person = self.out_list[i]
            print('姓名:{} 性别：{} 年龄：{}'.format(person.name, person.gender, person.age))
        print('幸存者：')
        survivor = self.survivor
        print('姓名:{} 性别：{} 年龄：{}'.format(survivor.name, survivor.gender, survivor.age))
