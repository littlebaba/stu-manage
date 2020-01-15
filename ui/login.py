import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *
import hashlib
import os


class Login(QWidget):
    is_admin_signal = pyqtSignal(str)

    def __init__(self):
        super(Login, self).__init__()
        self.resize(900, 600)
        self.setWindowTitle("欢迎使用学员管理系统")
        self.setup_ui()

    def setup_ui(self):
        self.Hlayout = QHBoxLayout(self)
        self.Vlayout = QVBoxLayout()

        self.formlayout = QFormLayout()
        self.label1 = QLabel("学号: ")
        self.lineEdit1 = QLineEdit()
        self.lineEdit1.setFixedHeight(32)
        self.lineEdit1.setFixedWidth(180)
        self.formlayout.addRow(self.label1, self.lineEdit1)

        self.label2 = QLabel("密码: ")
        self.lineEdit2 = QLineEdit()
        self.lineEdit2.setFixedHeight(32)
        self.lineEdit2.setFixedWidth(180)
        self.lineEdit2.setEchoMode(QLineEdit.Password)
        self.formlayout.addRow(self.label2, self.lineEdit2)

        self.signIn = QPushButton("登 录")
        self.signIn.setFixedWidth(80)
        self.signIn.setFixedHeight(30)
        self.formlayout.addRow("", self.signIn)

        self.widget2 = QWidget()
        self.widget2.setFixedWidth(300)
        self.widget2.setFixedHeight(150)
        self.widget2.setLayout(self.formlayout)
        self.Hlayout.addWidget(self.widget2)
        self.signIn.clicked.connect(self.login_check)

    def login_check(self):
        stu_num = self.lineEdit1.text()
        stu_pwd = self.lineEdit2.text()
        if stu_num == "" or stu_pwd == "":
            print(QMessageBox.warning(self, "警告", "学号和密码不能为空", QMessageBox.Yes, QMessageBox.Yes))
            return
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName('./db/lib_stu.db')
        dd = db.open()
        hn = db.hostName()
        query = QSqlQuery()
        sql = f"select s_num,s_pwd from student where student.s_num='{stu_num}'"
        query.exec_(sql)
        db.close()
        h1 = hashlib.md5()
        h1.update(stu_pwd.encode(encoding='utf-8'))
        if not query.next():
            print(QMessageBox.information(self, "提示", "该账号不存在！", QMessageBox.Yes, QMessageBox.Yes))
        else:
            if stu_num == query.value(0) and h1.hexdigest() == query.value(1):
                self.is_admin_signal.emit(stu_num)
            else:
                print(QMessageBox.information(self, "提示", "密码错误!", QMessageBox.Yes, QMessageBox.Yes))
        return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainWin = Login()
    mainWin.show()
    sys.exit(app.exec_())
