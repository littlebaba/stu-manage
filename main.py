import sys
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
import hashlib
import sip
from ui.login import Login
from ui.admin_home import AdminHome


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.layer = QHBoxLayout()
        self.widget = Login()
        self.resize(900, 600)
        self.setWindowTitle("欢迎登陆学员管理系统")
        self.setCentralWidget(self.widget)
        bar = self.menuBar()
        self.Menu = bar.addMenu("菜单栏")
        self.signUpAction = QAction("注册", self)
        self.changePasswordAction = QAction("修改密码", self)
        self.signInAction = QAction("登录", self)
        self.quitSignInAction = QAction("退出登录", self)
        self.quitAction = QAction("退出", self)
        self.Menu.addAction(self.signUpAction)
        self.Menu.addAction(self.changePasswordAction)
        self.Menu.addAction(self.signInAction)
        self.Menu.addAction(self.quitSignInAction)
        self.Menu.addAction(self.quitAction)
        self.signUpAction.setEnabled(True)
        self.changePasswordAction.setEnabled(True)
        self.signInAction.setEnabled(False)
        self.quitSignInAction.setEnabled(False)
        self.widget.is_admin_signal[str].connect(self.admin_sigin)
        self.Menu.triggered[QAction].connect(self.menu_triggered)

    def admin_sigin(self, admin_num):
        sip.delete(self.widget)
        self.widget = AdminHome(admin_num)
        self.setCentralWidget(self.widget)

    def menu_triggered(self, q):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = Main()
    mainWin.show()
    sys.exit(app.exec_())
