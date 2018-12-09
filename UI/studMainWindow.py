from PyQt5 import QtCore, QtGui, QtWidgets
from UI import studModInfo
'''
- 최초작성자 : 이영찬
- 최초작성일 : 2018.11.29
- 최초변경일 : 2018.12.06
- 목적 : 학생의 로그인 이후 화면
- 개정이력 : 이영찬, 2018.12.06
'''
class view_studMainWindow(object):
    def __init__(self, InfoList, stud, state):
        self.list = InfoList
        self.__dialog = None
        self.owner = stud
        self.state = state
        self.isnew = True

    def setupUi(self, Mainwindow):
        Mainwindow.setObjectName("MainWindow")
        Mainwindow.resize(423, 411)
        self.centralwidget = QtWidgets.QWidget(Mainwindow)
        self.centralwidget.setObjectName("centralwidget")
        #self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        #self.pushButton.setGeometry(QtCore.QRect(9, 9, 75, 23))
        #self.pushButton.setObjectName("탈퇴")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 10, 75, 23))
        self.pushButton_2.setObjectName("정보수정")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(9, 38, 401, 361))
        self.tableWidget.setObjectName("리스트")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(len(self.list))
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        #self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        #self.pushButton_3.setGeometry(QtCore.QRect(250, 10, 75, 23))
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 10, 151, 21))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("State")
        Mainwindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Mainwindow)
        self.statusbar.setObjectName("statusbar")

        Mainwindow.setStatusBar(self.statusbar)
        self.tableWidget.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        self.__dialog=Mainwindow
        if self.isnew == True:

            self.setTableWidgetData()
            self.isnew = False
        else:
            self.refreshList()

        self.retranslateUi(Mainwindow)
        # 탈퇴 버튼 클릭 시 팀 탈퇴 기능을 수행
        #self.pushButton.clicked.connect(self.quitButtonClicked)
        # 정보수정 버튼 클릭 시 정보 수정 인터페이스 및 함수 호출
        self.pushButton_2.clicked.connect(self.modButtonClicked)
        # 신청 버튼 클릭 시 해당 학생에게 가입 요청 메시지를 전달
        #self.pushButton_3.clicked.connect(self.joinButtonClicked)
        self.tableWidget.activated['QModelIndex'].connect(self.tableWidget.update)
        QtCore.QMetaObject.connectSlotsByName(Mainwindow)

    #목적 : 테이블에 수업을 듣는 학생들의 정보을 출력 [팀 번호는 출력하지 않는다]
    def setTableWidgetData(self):
        print("테이블 정보 입력")
        for row in range(len(self.list)):
            item = QtWidgets.QTableWidgetItem(self.list[row].studentName)
            self.tableWidget.setItem(row, 0, item)
            item = QtWidgets.QTableWidgetItem(self.list[row].studentPhone)
            self.tableWidget.setItem(row, 1, item)
            item = QtWidgets.QTableWidgetItem(self.list[row].studentTeamNo)
            self.tableWidget.setItem(row, 2, item)
            self.tableWidget.setSortingEnabled(True)
            item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight)
        self.label.setText("state : " + str(self.state))

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

    # 목적: 팀을 탈퇴하기 위한 함수 실행을 요청
    def quitButtonClicked(self):
        to = self.tableWidget.curruntRow()
        print("학생팀탈퇴")
        self.owner.quitTeam(to)

    # 목적 : 정보를 수정하기 위한 인터페이스를 띄운다.
    def modButtonClicked(self):
        print("학생정보수정")
        dialog = QtWidgets.QDialog()

        ui = studModInfo.view_studModInfo(self.owner)
        ui.setupUi(dialog)
        dialog.exec()

    # 목적 : 원하는 사람에게 팀 가입 신청 메시지를 보낸다.
    def joinButtonClicked(self):
        to = self.tableWidget.curruntRow()
        print("가입신청")
        self.owner.wantJoin(to)

    #목적 : 변동된 리스트 정보를 띄운다.
    def updateList(self, list, state):
        self.list = list
        self.state = state

    def refreshList(self):
        for row in range(len(self.list)):
            item = QtWidgets.QTableWidgetItem(self.list[row].studentNo)
            self.tableWidget.setItem(row, 0, item)
            item = QtWidgets.QTableWidgetItem(self.list[row].studentName)
            self.tableWidget.setItem(row, 1, item)
            item = QtWidgets.QTableWidgetItem(self.list[row].studentPhone)
            self.tableWidget.setItem(row, 2, item)
            self.tableWidget.setSortingEnabled(True)
            item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight)

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        self.label.setText("state : " + str(self.state))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ModStudInfo"))
        #self.pushButton.setAccessibleName(_translate("MainWindow", "leaveTeam_Button"))
        #self.pushButton.setText(_translate("MainWindow", "탈퇴"))
        #self.pushButton_2.setAccessibleName(_translate("MainWindow", "modInfo_Button"))
        self.pushButton_2.setText(_translate("MainWindow", "정보수정"))
        self.tableWidget.setAccessibleName(_translate("MainWindow", "InfoList"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "이름"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "연락처"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "팀번호"))
        #self.pushButton_3.setAccessibleName(_translate("MainWindow", "join_Button"))
        #self.pushButton_3.setText(_translate("MainWindow", "신청"))

if __name__ == "__main__":
    import sys
    import os


    class std:
        studentNo = "0"
        studentName = "test"
        studentPhone = "000"
        studentTeamNo = "1"

    mypath = os.path.dirname(sys.executable) + "\Lib\site-packages\PyQt5\Qt\plugins"
    libpaths = QtWidgets.QApplication.libraryPaths()
    libpaths.append(mypath)
    QtWidgets.QApplication.setLibraryPaths(libpaths)
    stdd = []
    stdd.append(std())

    app = QtWidgets.QApplication(sys.argv)
    MainWindows = QtWidgets.QMainWindow()
    ui = view_studMainWindow(stdd,"a",True)
    ui.setupUi(MainWindows)
    MainWindows.show()
    sys.exit(app.exec_())

