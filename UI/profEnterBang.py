from PyQt5 import QtCore, QtGui, QtWidgets
from UI import profMakeBang
from pyqt5plus import *
import InitializeManager
import os, sys

'''
최초작성자 : 이영찬
최초작성일 : 2018.11.29
최초변경일 : 2018.12.06
목적 : 교수의 방 입장
개정이력 : 이영찬, 2018.12.06
'''

class view_EnterBang(QtWidgets.QDialog):
    def __init__(self, bangIndex, bangList, prof, parent = None):
        super(view_EnterBang, self).__init__(parent)
        self.list = bangList
        self.index = bangIndex
        self.__dialog = None
        self.owner = prof

    def setupUi(self, Dialog):
        Dialog.setObjectName("Title")
        Dialog.resize(402, 550)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어 ExtraBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어라운드 Bold")
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(len(self.index))
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("추가")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setObjectName("입장")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.retranslateUi(Dialog)
        self.__dialog = Dialog

        self.setTableWidgetData()
        # 추가 버튼 입력시 새로운 윈도우를 뛰워야 함.
        self.pushButton.clicked.connect(self.addButtonClicked)
        self.pushButton_2.clicked.connect(self.enterButtonClicked)

        self.tableWidget.itemDoubleClicked['QTableWidgetItem*'].connect(self.doubleButtonClicked)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def setTableWidgetData(self):
        list = self.list

        for row in range(len(list)):
            item = QtWidgets.QTableWidgetItem(str(self.index[row]))
            self.tableWidget.setItem(row, 0, item)
            item = QtWidgets.QTableWidgetItem(list[row].getSubjName())
            self.tableWidget.setItem(row, 1, item)
            self.tableWidget.setSortingEnabled(True)
            item.setTextAlignment(QtCore.Qt.AlignRight)

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

    def addButtonClicked(self):
        dialog = QtWidgets.QDialog()
        ui = profMakeBang.view_makebang(self.owner)
        ui.setupUi(dialog)
        dialog.show()

    #목적 : 변동된 리스트 정보를 띄운다.
    def updateList(self, list):
        for row in range(len(list)):
            item = QtWidgets.QTableWidgetItem(self.index[row])
            self.tableWidget.setItem(row, 0, item)
            item = QtWidgets.QTableWidgetItem(list[row])
            self.tableWidget.setItem(row, 1, item)
            self.tableWidget.setSortingEnabled(True)
            item.setTextAlignment(QtCore.Qt.AlignVcenter | QtCore.Qt.AlignRight)

        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

    def doubleButtonClicked(self):
        idx = self.tableWidget.currentRow()
        idx = self.index[idx]
        self.owner.enterBang(idx)
        self.__dialog.close()

    def enterButtonClicked(self):
        idx = self.tableWidget.currentRow()
        idx = self.index[idx]
        self.owner.enterBang(idx)
        self.__dialog.close()

    def retranslateUi(self, Title):
        _translate = QtCore.QCoreApplication.translate
        Title.setWindowTitle(_translate("Title", "Software_Engineering"))
        self.label.setText(_translate("Title", "방 목록"))
        self.tableWidget.setAccessibleName(_translate("Title", "BangList"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Title", "방 번호"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Title", "수업이름"))
        self.pushButton.setAccessibleName(_translate("Title", "addBang_Button"))
        self.pushButton.setText(_translate("Title", "추가"))
        self.pushButton_2.setAccessibleName(_translate("Title", "EnterBang_Button"))
        self.pushButton_2.setText(_translate("Title", "입장"))

class test:
    SubjName = "test"

    def getSubjName(self):
        return self.SubjName

if __name__ == "__main__":
    import sys
    import os
    mypath = os.path.dirname(sys.executable) + "\Lib\site-packages\PyQt5\Qt\plugins"
    libpaths = QtWidgets.QApplication.libraryPaths()
    libpaths.append(mypath)
    QtWidgets.QApplication.setLibraryPaths(libpaths)

    t = test()
    tlist = []
    tlist.append(t)
    app = QtWidgets.QApplication(sys.argv)
    Title = QtWidgets.QDialog()
    #Title = view_EnterBang([0],[0],"a")
    ui = view_EnterBang([0],tlist,"a")
    ui.setupUi(Title)
    Title.show()
    sys.exit(app.exec_())

