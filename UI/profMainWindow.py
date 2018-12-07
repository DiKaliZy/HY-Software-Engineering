from PyQt5 import QtCore, QtGui, QtWidgets

'''
최초작성자 : 이영찬
최초작성일 : 2018.11.29
최초변경일 :
목적 : 교수의 방 입장 후 메인화면 출력
개정이력:
'''
class view_ProfMainWindow(object):
    def __init__(self, Infolist):
        self.list = Infolist

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(543, 590)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.gridLayout.addWidget(self.tableWidget, 2, 0, 1, 2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.tableWidget.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        self.setTableWidgetData()
        idx = self.tableWidget.curruntRow()

        self.retranslateUi(MainWindow)
        #추가 버튼 클릭 시 addButtonClicked 함수 호출
        self.pushButton.clicked.connect(self.addButtonClicked)
        #설정 버튼 클릭 시 setButtonClicked 함수 호출
        self.pushButton_2.clicked.connect(self.setButtonClicked)
        #ON/OFF 버튼 클릭 시 switButtonClicked 함수 호출
        self.pushButton_3.clicked.connect(self.switButtonClicked)
        #수정 버튼 클릭 시 modButtonClicked 함수 호출
        self.pushButton_4.clicked.connect(self.modButtonClicked)
        #삭제 버튼 클릭 시 delButtonClicked 함수 호출
        self.pushButton_5.clicked.connect(self.delButtonClicked(idx))
        self.tableWidget.activated['QModelIndex'].connect(self.tableWidget.update)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #목적 : 테이블의 내용을 채운다.
    def setTableWidgetData(self):
        list = self.list
        for row in range(len(list)):
            item = QtWidgets.QTableWidgetItem(list[row].studentNo)
            self.tableWidget.setItem(row, 0, item)
            item = QtWidgets.QTableWidgetItem(list[row].studentName)
            self.tableWidget.setItem(row, 1, item)
            item = QtWidgets.QTableWidgetItem(list[row].studentPhone)
            self.tableWidget.setItem(row, 2, item)
            item = QtWidgets.QTableWidgetItem(list[row].studentTeamNo)
            self.tableWidget.setItem(row, 3, item)
            self.tableWidget.setSortingEnabled(True)
            item.setTextAlignment(QtCore.Qt.AlignVcenter | QtCore.Qt.AlignRight)


        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()


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
        self.label.setText("state : ", state)

    #목적 : 학생 정보를 수정하기 위한 인터페이스를 띄우도록 요청한다.
    def modButtonClicked(self):
        window = view_profModInfo()
        window.show()

    #목적 : 학생 정보를 삭제하기 위한 인터페이스를 띄우도록 요청한다.
    def delButtonClicked(self,idx):
        professor.deleteStud(idx)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "메인화면"))
        self.tableWidget.setAccessibleName(_translate("MainWindow", "InfoList"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "학번"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "이름"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "연락처"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "팀번호"))
        self.pushButton_3.setAccessibleName(_translate("MainWindow", "switch_button"))
        self.pushButton_3.setText(_translate("MainWindow", "ON/OFF"))
        self.pushButton.setAccessibleName(_translate("MainWindow", "add_Button"))
        self.pushButton.setText(_translate("MainWindow", "추가"))
        self.pushButton_2.setAccessibleName(_translate("MainWindow", "set_Button"))
        self.pushButton_2.setText(_translate("MainWindow", "설정"))
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

