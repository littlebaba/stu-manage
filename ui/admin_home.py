import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class AdminHome(QWidget):
    def __init__(self, admin_num):
        super(AdminHome, self).__init__()
        self.setup_ui()

    def setup_ui(self):
        self.resize(900, 600)
        self.setWindowTitle("欢迎使用图书馆管理系统")
        self.layout = QHBoxLayout()
        self.buttonlayout = QVBoxLayout()
        self.setLayout(self.layout)

        font = QFont()
        font.setPixelSize(16)
        self.userManageButton = QPushButton("用户管理")
        self.addBookButton = QPushButton("添加书籍")
        self.dropBookButton = QPushButton("淘汰书籍")
        self.userManageButton.setFont(font)
        self.addBookButton.setFont(font)
        self.dropBookButton.setFont(font)
        self.userManageButton.setFixedWidth(100)
        self.userManageButton.setFixedHeight(42)
        self.addBookButton.setFixedWidth(100)
        self.addBookButton.setFixedHeight(42)
        self.dropBookButton.setFixedWidth(100)
        self.dropBookButton.setFixedHeight(42)
        self.buttonlayout.addWidget(self.addBookButton)
        self.buttonlayout.addWidget(self.dropBookButton)
        self.buttonlayout.addWidget(self.userManageButton)
        self.layout.addLayout(self.buttonlayout)
        # self.storageView = BookStorageViewer()
        # self.layout.addWidget(self.storageView)
        #
        # self.addBookButton.clicked.connect(self.addBookButtonClicked)
        # self.dropBookButton.clicked.connect(self.dropBookButtonClicked)
        # self.userManageButton.clicked.connect(self.userManage)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mian_win = AdminHome("1001")
    mian_win.show()
    sys.exit(app.exec_())
