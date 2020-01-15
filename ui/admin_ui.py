import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(90, 80, 571, 431))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(20, 40, 511, 321))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setLineWidth(1)
        self.label.setMidLineWidth(0)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.name_edit = QtWidgets.QLineEdit(self.widget)
        self.name_edit.setObjectName("name_edit")
        self.gridLayout.addWidget(self.name_edit, 0, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.widget)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 0, 2, 1, 1)
        self.studentid_edit = QtWidgets.QLineEdit(self.widget)
        self.studentid_edit.setObjectName("studentid_edit")
        self.gridLayout.addWidget(self.studentid_edit, 0, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.id_edit = QtWidgets.QLineEdit(self.widget)
        self.id_edit.setObjectName("id_edit")
        self.gridLayout.addWidget(self.id_edit, 1, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.widget)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 1, 2, 1, 1)
        self.tel_edit = QtWidgets.QLineEdit(self.widget)
        self.tel_edit.setObjectName("tel_edit")
        self.gridLayout.addWidget(self.tel_edit, 1, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.trainorder_edit = QtWidgets.QLineEdit(self.widget)
        self.trainorder_edit.setObjectName("trainorder_edit")
        self.gridLayout.addWidget(self.trainorder_edit, 2, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.widget)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 2, 2, 1, 1)
        self.traintype_edit = QtWidgets.QLineEdit(self.widget)
        self.traintype_edit.setObjectName("traintype_edit")
        self.gridLayout.addWidget(self.traintype_edit, 2, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.traintime_edit = QtWidgets.QLineEdit(self.widget)
        self.traintime_edit.setObjectName("traintime_edit")
        self.gridLayout.addWidget(self.traintime_edit, 3, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.widget)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 3, 2, 1, 1)
        self.gender_edit = QtWidgets.QLineEdit(self.widget)
        self.gender_edit.setObjectName("gender_edit")
        self.gridLayout.addWidget(self.gender_edit, 3, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.edu_edit = QtWidgets.QLineEdit(self.widget)
        self.edu_edit.setObjectName("edu_edit")
        self.gridLayout.addWidget(self.edu_edit, 4, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.widget)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 4, 2, 1, 1)
        self.service_edit = QtWidgets.QLineEdit(self.widget)
        self.service_edit.setObjectName("service_edit")
        self.gridLayout.addWidget(self.service_edit, 4, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.unit_edit = QtWidgets.QLineEdit(self.widget)
        self.unit_edit.setObjectName("unit_edit")
        self.gridLayout.addWidget(self.unit_edit, 5, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.widget)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 5, 2, 1, 1)
        self.position_edit = QtWidgets.QLineEdit(self.widget)
        self.position_edit.setObjectName("position_edit")
        self.gridLayout.addWidget(self.position_edit, 5, 3, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableView = QtWidgets.QTableView(self.tab_2)
        self.tableView.setGeometry(QtCore.QRect(100, 120, 256, 192))
        self.tableView.setObjectName("tableView")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_19.setGeometry(QtCore.QRect(110, 40, 171, 21))
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        self.pushButton.setGeometry(QtCore.QRect(290, 40, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_20.setGeometry(QtCore.QRect(120, 30, 171, 21))
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 30, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "姓名"))
        self.label_18.setText(_translate("MainWindow", "学号"))
        self.label_2.setText(_translate("MainWindow", "身份证号"))
        self.label_13.setText(_translate("MainWindow", "电话"))
        self.label_3.setText(_translate("MainWindow", "培训班次"))
        self.label_15.setText(_translate("MainWindow", "培训类型"))
        self.label_4.setText(_translate("MainWindow", "培训时长"))
        self.label_14.setText(_translate("MainWindow", "性别"))
        self.label_5.setText(_translate("MainWindow", "文化程度"))
        self.label_16.setText(_translate("MainWindow", "军种"))
        self.label_6.setText(_translate("MainWindow", "单位"))
        self.label_17.setText(_translate("MainWindow", "职务"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "增加"))
        self.pushButton.setText(_translate("MainWindow", "搜索"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "删除"))
        self.pushButton_2.setText(_translate("MainWindow", "搜索"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "修改"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mian_win = Ui_MainWindow()
    mian_win.show()
    sys.exit(app.exec_())