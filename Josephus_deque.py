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

    def add_one_person(self, new_person):
        self.append(new_person)

    def add_persons(self, reader):
        reader.read_person_info()
        self.extend(reader.persons)

    def delete_person(self):
        self.rotate(-self.step)
        out_person = self.pop()
        return out_person

    def find_start_pos(self):
        self.rotate(-self.start_pos)
        self.start_pos = None

    def __iter__(self):
        return self

    def __next__(self):
        if len(self) == 1:
            self.survivor = self.pop()
            return self.survivor
        elif len(self) == 0:
            raise StopIteration

        if self.start_pos is not None:
            # 旋转到指定位置
            self.find_start_pos()

        out_person = self.delete_person()
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

