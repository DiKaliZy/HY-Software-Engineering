# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Teamsetting.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class view_TeamSetting(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(308, 159)
        Dialog.setAcceptDrops(False)
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(240, 40, 61, 51))
        self.spinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spinBox.setObjectName("spinBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 40, 171, 51))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어라운드 ExtraBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(30, 120, 75, 23))
        self.pushButton.setObjectName("확인")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 120, 75, 23))
        self.pushButton_2.setObjectName("취소")

        limit = int(self.spinBox.text())
        self.retranslateUi(Dialog)
        #확인 버특 클릭 시 입력된 값을 매개변수로 한 limit 함수를 호출한다.
        self.pushButton.clicked.connect(self.okayButtonClicked(limit))
        self.pushButton_2.clicked.connect(self.close())
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def okayButtonClicked(self, limit):
        professor.setlimit(limit)
        self.close()


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "TeamSetting"))
        self.spinBox.setAccessibleName(_translate("Dialog", "limitnum"))
        self.label.setText(_translate("Dialog", "인원설정"))
        self.pushButton.setText(_translate("Dialog", "확인"))
        self.pushButton_2.setText(_translate("Dialog", "취소"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = view_TeamSetting()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

