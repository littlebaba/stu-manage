import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class StudentHome(QWidget):
    def __init__(self, stu_num):
        super(StudentHome, self).__init__()
        self.resize(900, 600)
        self.setWindowTitle("欢迎使用图书馆管理系统")
        self.setup_ui()
    def setup_ui(self):
        # 总布局
        self.layout = QHBoxLayout(self)
        # 按钮布局
        self.buttonLayout = QVBoxLayout()
        # 按钮
        self.borrowBookButton = QPushButton("借书")
        self.returnBookButton = QPushButton("还书")
        self.myBookStatus = QPushButton("借阅状态")
        self.allBookButton = QPushButton("所有书籍")
        self.buttonLayout.addWidget(self.borrowBookButton)
        self.buttonLayout.addWidget(self.returnBookButton)
        self.buttonLayout.addWidget(self.myBookStatus)
        self.buttonLayout.addWidget(self.allBookButton)
        self.borrowBookButton.setFixedWidth(100)
        self.borrowBookButton.setFixedHeight(42)
        self.returnBookButton.setFixedWidth(100)
        self.returnBookButton.setFixedHeight(42)
        self.myBookStatus.setFixedWidth(100)
        self.myBookStatus.setFixedHeight(42)
        self.allBookButton.setFixedWidth(100)
        self.allBookButton.setFixedHeight(42)
        font = QFont()
        font.setPixelSize(16)
        self.borrowBookButton.setFont(font)
        self.returnBookButton.setFont(font)
        self.myBookStatus.setFont(font)
        self.allBookButton.setFont(font)

        # self.storageView = BookStorageViewer()
        # self.borrowStatusView = BorrowStatusViewer(self.StudentId)
        self.allBookButton.setEnabled(False)

        self.layout.addLayout(self.buttonLayout)
        # self.layout.addWidget(self.storageView)