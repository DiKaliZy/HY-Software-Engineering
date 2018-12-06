# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'profMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class view_ProfMainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(452, 449)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 158, 25))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("추가")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("설정")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(360, 10, 75, 23))
        self.pushButton_3.setObjectName("ON/OFF")
        self.pushButton_3.setCheckable(True)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(9, 40, 431, 381))
        self.tableWidget.setObjectName("명단 리스트")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(410, 40, 151, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_4.setObjectName("수정")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_5.setObjectName("삭제")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(380, 10, 101, 21))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        #추가 버튼 클릭 시 addButtonClicked 함수 호출
        self.pushButton.clicked.connect(self.addButtonClicked)
        #설정 버튼 클릭 시 setButtonClicked 함수 호출
        self.pushButton_2.clicked.connect(self.setButtonClicked)
        #ON/OFF 버튼 클릭 시 switButtonClicked 함수 호출
        self.pushButton_3.toggled.connect(self.switButtonClicked)
        #수정 버튼 클릭 시 modButtonClicked 함수 호출
        self.pushButton_4.clicked.connect(self.modButtonClicked)
        #삭제 버튼 클릭 시 delButtonClicked 함수 호출
        self.pushButton_5.clicked.connect(self.delButtonClicked)
        self.tableWidget.activated['QModelIndex'].connect(self.tableWidget.update)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #목적 : 새로운 학생을 리스트에 추가하기 위한 추가 인터페이스를 띄우도록 요청한다.
    def addButtonClicked(self):
        window = view_addStudent()
        window.show()

    #목적 : 팀 조건을 바꾸기 위해 팀 조건 설정 인터페이스를 띄우도록 요청한다.
    def setButtonClicked(self):
        window = view_TeamSetting()
        window.show()

    #목적 : 팀 구성 가능 여부를 바꾼다.
    def switButtonClicked(self):
        Professor.swtichOper()
        state = display.switchOnOff()
        self.label.setText(state)

    #목적 : 학생 정보를 수정하기 위한 인터페이스를 띄우도록 요청한다.
    def modButtonClicked(self):
        self.close()
    #목적 : 학생 정보를 삭제하기 위한 인터페이스를 띄우도록 요청한다.
    def delButtonClicked(self):
        self.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "메인화면"))
        self.pushButton.setAccessibleName(_translate("MainWindow", "add_Button"))
        self.pushButton.setText(_translate("MainWindow", "추가"))
        self.pushButton_2.setAccessibleName(_translate("MainWindow", "set_Button"))
        self.pushButton_2.setText(_translate("MainWindow", "설정"))
        self.pushButton_3.setAccessibleName(_translate("MainWindow", "switch_button"))
        self.pushButton_3.setText(_translate("MainWindow", "ON/OFF"))
        self.tableWidget.setAccessibleName(_translate("MainWindow", "InfoList"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "학번"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "이름"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "연락처"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "팀번호"))
        self.pushButton_4.setAccessibleName(_translate("MainWindow", "ModButton"))
        self.pushButton_4.setText(_translate("MainWindow", "수정"))
        self.pushButton_5.setAccessibleName(_translate("MainWindow", "delButton"))
        self.pushButton_5.setText(_translate("MainWindow", "삭제"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = view_ProfMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

