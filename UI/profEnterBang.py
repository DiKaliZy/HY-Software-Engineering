# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'profEnterBang.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class view_EnterBang(object):

    def setupUi(self, mainWindow):
        mainWindow.setObjectName("Title")
        mainWindow.resize(402, 550)
        self.verticalLayout = QtWidgets.QVBoxLayout(Title)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Title)
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어 ExtraBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tableWidget = QtWidgets.QTableWidget(Title)
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어라운드 Bold")
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(Title)
        self.pushButton.setObjectName("추가")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(Title)
        self.pushButton_2.setObjectName("입장")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Title)


        #추가 버튼 입력시 새로운 윈도우를 뛰워야 함.
        self.setTableWidgetData()
        self.pushButton.clicked.connect(self.addButtonClicked)
        self.pushButton_2.clicked.connect(self.enterButtonClicked(idx))
        self.tableWidget.itemClicked['QTableWidgetItem*'].connect(self.pushButton_2.click)
        QtCore.QMetaObject.connectSlotsByName(Title)

    def setTableWidgetData(self):
        banglist = display.refreshbang()
        column_idx = {'num': 0, 'name': 1}
        for k, v in banglist.item():
            col = column_idx[k]
            for row, val in enumerate(v):
                item = QtWidgets.QTableWidgetItem(val)
                if col == 2:
                    item.setTextAlignment(QtCore.Qt.AlignVcenter|QtCore.Qt.AlignRight)

    def addButtonClicked(self):
        window = view_makebang()
        window.show()

    def enterBunttonClicked(self, idx):
        Professor.enterBang(idx)
        self.close()

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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Title = view_EnterBang()
    ui = view_EnterBang()
    ui.setupUi(Title)
    Title.show()
    sys.exit(app.exec_())

