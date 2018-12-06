from PyQt5 import QtCore, QtGui, QtWidgets
'''
최초작성자 : 이영찬
최초작성일 : 2018.11.29
최초변경일 :
목적 : 학생의 로그인 이후 화면
개정이력:
'''
class view_studMainWindow(object):
    def setupUi(self, Mainwindow):
        Mainwindow.setObjectName("Dialog")
        Mainwindow.resize(423, 411)
        self.centralwidget = QtWidgets.QWidget(Dialog)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(9, 9, 75, 23))
        self.pushButton.setObjectName("탈퇴")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 10, 75, 23))
        self.pushButton_2.setObjectName("정보수정")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(9, 38, 401, 361))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(320, 70, 75, 23))
        self.pushButton_3.setObjectName("신청")

        to = self.tableWidget.itemClicked(1)
        self.retranslateUi(MainWindow)
        # 탈퇴 버튼 클릭 시 팀 탈퇴 기능을 수행
        self.pushButton.clicked.connect(self.quitButtonClicked)

        # 정보수정 버튼 클릭 시 정보 수정 인터페이스 및 함수 호출
        self.pushButton_2.clicked.connect(self.modButtonClicked)

        # 신청 버튼 클릭 시 해당 학생에게 가입 요청 메시지를 전달
        self.pushButton_3.clicked.connect(self.joinButtonClicked(to))
        self.tableWidget.activated['QModelIndex'].connect(self.tableWidget.update)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # 목적: 팀을 탈퇴하기 위한 함수 실행을 요청
    def quitButtonClicked(self):
        student.quitTeam()

    # 목적 : 정보를 수정하기 위한 인터페이스를 띄운다.
    def modButtonClicked(self):
        window = studModInfo()
        window.show()

    # 목적 : 원하는 사람에게 팀 가입 신청 메시지를 보낸다.
    def joinButtonClicked(self, to):
        student.wantJoin(to)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ModStudInfo"))
        self.pushButton.setAccessibleName(_translate("MainWindow", "leaveTeam_Button"))
        self.pushButton.setText(_translate("MainWindow", "탈퇴"))
        self.pushButton_2.setAccessibleName(_translate("MainWindow", "modInfo_Button"))
        self.pushButton_2.setText(_translate("MainWindow", "정보수정"))
        self.tableWidget.setAccessibleName(_translate("MainWindow", "InfoList"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "이름"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "연락처"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "팀번호"))
        self.pushButton_3.setAccessibleName(_translate("MainWindow", "join_Button"))
        self.pushButton_3.setText(_translate("MainWindow", "신청"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = view_studMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

