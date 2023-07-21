import unittest
from TestJosephus import TestJosephus


if __name__ == '__main__':
    # 构造测试集，实例化测试套件
    suite = unittest.TestSuite()
    # 执行顺序为安装加载顺序
    suite.addTest(TestJosephus("test_add_one_person"))
    suite.addTest(TestJosephus("test_delete_person"))
    suite.addTest(TestJosephus("test_read_person_info_from_txt"))
    suite.addTest(TestJosephus("test_read_person_info_from_txt"))
    suite.addTest(TestJosephus("test_read_person_info_from_zip"))
    suite.addTest(TestJosephus("test_josephus_txt"))
    suite.addTest(TestJosephus("test_josephus_csv"))
    suite.addTest(TestJosephus("test_josephus_zip"))
    # 执行测试，将测试结果输入到test.txt文件中
    with open('test_result.txt', 'a') as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        runner.run(suite)
