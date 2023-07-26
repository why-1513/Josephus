from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QFileDialog, \
    QMessageBox, QInputDialog, QTableWidget, QTableWidgetItem, QLineEdit
from Josephus_deque import Josephus
from TxtReader import TxtReader
from ZipReader import ZipReader
from CsvReader import CsvReader
from GetInput import start_get_input
import sys
import logging


class JosephusChooser(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Josephus Chooser')
        self.setGeometry(800, 400, 480, 150)

        # 创建选择文件框
        self.file_label = QLabel('File:', self)
        self.file_label.move(50, 25)
        self.file_text = QLineEdit(self)
        self.file_text.move(90, 25)
        self.file_text.resize(240, 25)  # 调整文本框大小
        self.file_button = QPushButton('Select File', self)
        self.file_button.move(350, 25)
        self.file_button.resize(80, 25)  # 调整按钮大小
        self.file_button.setFont(QFont("Arial", 10))  # 设置字体
        self.file_button.clicked.connect(self.select_file)

        # 创建选择程序类型按钮
        self.gui_button = QPushButton('GUI', self)
        self.gui_button.move(100, 85)
        self.file_label.setFont(QFont("Arial", 14))  # 设置字体
        self.gui_button.resize(100, 25)  # 调整按钮大小
        self.gui_button.setFont(QFont("Arial", 10))  # 设置字体
        self.gui_button.clicked.connect(self.run_gui)
        self.console_button = QPushButton('Console', self)
        self.console_button.move(280, 85)
        self.console_button.resize(100, 25)  # 调整按钮大小
        self.console_button.setFont(QFont("Arial", 10))  # 设置字体
        self.console_button.clicked.connect(self.run_console)

        self.result_window = None
        self.setFixedSize(self.size())  # 固定窗口大小
        self.show()

    def select_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Select File", "", "All Files (*);;Text Files (*.txt);;CSV Files (*.csv);;Zip Files (*.zip)",
            options=options)
        if file_name:
            self.file_text.setText(file_name)

    def run_gui(self):
        file_name = self.file_text.text()
        if not file_name:
            QMessageBox.warning(self, 'Warning', 'Please select a file')
            logging.error('From run_gui: Please select a file')
            return
        elif file_name.endswith('.txt'):
            reader = TxtReader(file_name)
        elif file_name.endswith('.csv'):
            reader = CsvReader(file_name)
        elif file_name.endswith('.zip'):
            reader = ZipReader(file_name)
        else:
            QMessageBox.warning(self, 'Warning', 'Unsupported file type')
            logging.error('From run_gui: Unsupported file type')
            return

        step_num, ok = QInputDialog.getInt(self, 'Step Number', 'Enter the step number:')
        if not ok:
            return
        while step_num <= 0:
            QMessageBox.warning(self, 'Warning', 'Please enter a non-negative integer')
            logging.error('From run_gui: Please enter a non-negative integer')
            step_num, ok = QInputDialog.getInt(self, 'Step Number', 'Enter the step number:')
            if not ok:
                return

        start_pos, ok = QInputDialog.getInt(self, 'Start Position', 'Enter the start position:')
        if not ok:
            return
        while start_pos < 0:
            QMessageBox.warning(self, 'Warning', 'Please enter a non-negative integer')
            logging.error('From run_gui: Please enter a non-negative integer')
            start_pos, ok = QInputDialog.getInt(self, 'Start Position', 'Enter the start position:')
            if not ok:
                return

        josephus = Josephus(step_num, start_pos)
        josephus.add_persons(reader)
        for person in josephus:
            pass

        # 显示结果
        self.result_window = ResultWindow(out_list=josephus.out_list, survivor=josephus.survivor)
        self.result_window.show()

    def run_console(self):
        file_name = self.file_text.text()
        if not file_name:
            logging.error('Please select a file')
            print('From run_console: Please select a file')
            return
        elif file_name.endswith('.txt'):
            reader = TxtReader(file_name)
        elif file_name.endswith('.csv'):
            reader = CsvReader(file_name)
        elif file_name.endswith('.zip'):
            reader = ZipReader(file_name)
        else:
            logging.error('Unsupported file type')
            print('From run_console: Unsupported file type')
            return

        step_num, start_pos = start_get_input()
        if step_num is None or start_pos is None:
            return

        josephus = Josephus(step_num, start_pos)
        josephus.add_persons(reader)
        for person in josephus:
            pass
        josephus.josephus_print()


class ResultWindow(QWidget):
    def __init__(self, out_list, survivor):
        super().__init__()
        self.setWindowTitle('Josephus Result')
        self.setGeometry(100, 100, 400, 400)

        # 创建表格控件并设置列数
        table = QTableWidget(self)
        table.setColumnCount(4)

        # 设置表头
        table.setHorizontalHeaderLabels(['name', 'gender', 'age', 'State'])

        # 将淘汰者信息添加到表格中
        for i, item in enumerate(out_list):
            table.insertRow(i)
            table.setItem(i, 0, QTableWidgetItem(item.name))
            table.setItem(i, 1, QTableWidgetItem(item.gender))
            table.setItem(i, 2, QTableWidgetItem(str(item.age)))
            table.setItem(i, 3, QTableWidgetItem('Loser'))

        # 将幸存者信息添加到表格中
        if survivor is not None:
            table.insertRow(len(out_list))
            table.setItem(len(out_list), 0, QTableWidgetItem(survivor.name))
            table.setItem(len(out_list), 1, QTableWidgetItem(survivor.gender))
            table.setItem(len(out_list), 2, QTableWidgetItem(str(survivor.age)))
            table.setItem(len(out_list), 3, QTableWidgetItem('Survivor'))

        # 调整表格大小并创建布局
        table.resizeColumnsToContents()
        layout = QVBoxLayout()
        layout.addWidget(table)
        self.setLayout(layout)
        self.setFixedSize(self.size())  # 固定窗口大小
        self.show()


if __name__ == '__main__':
    logging.basicConfig(filename='test.log', filemode='a',
                        format='%(asctime)s [%(levelname)s] %(message)s', level=logging.INFO)
    app = QApplication(sys.argv)
    chooser = JosephusChooser()
    sys.exit(app.exec_())
