# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'message.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class view_Message(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(413, 143)
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
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("승락")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setObjectName("거절")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)

        #from =

        # 승락 버튼 클릭 시 positive메서드 호출
        self.pushButton.clicked.connect(stud.positive(from))
        # 거절 버튼 클릭 시 negative메서드 호출
        self.pushButton_2.clicked.connect(stud.negative(from))
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Message"))
        self.label.setAccessibleName(_translate("Dialog", "JoinMessage"))
        self.label.setText(_translate("Dialog", "OOO 으로부터 팀 가입 신청이 왔습니다."))
        self.pushButton.setAccessibleName(_translate("Dialog", "positive_button"))
        self.pushButton.setText(_translate("Dialog", "승락"))
        self.pushButton_2.setAccessibleName(_translate("Dialog", "negative_button"))
        self.pushButton_2.setText(_translate("Dialog", "거절"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = view_Message()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

