from PyQt5 import QtCore, QtGui, QtWidgets
'''
최초작성자 : 이영찬
최초작성일 : 2018.11.29
최초변경일 :
목적 : 에러 메시지 생성
개정 이력 :
'''
class view_ErrorMsg(object):
    def setupUi(self, Error):
        Error.setObjectName("Error")
        Error.resize(457, 138)
        self.verticalLayout = QtWidgets.QVBoxLayout(Error)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Error)
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어라운드 ExtraBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(Error)
        self.pushButton.setObjectName("확인")
        self.verticalLayout.addWidget(self.pushButton)

        self.retranslateUi(Error)
        self.pushButton.clicked.connect(Error.accept)
        QtCore.QMetaObject.connectSlotsByName(Error)

    #목적 : 메시지의 내용을 설정한다.
    def setMessage(self, context):
        self.label.setText(context)

    def retranslateUi(self, Error):
        _translate = QtCore.QCoreApplication.translate
        Error.setWindowTitle(_translate("Error", "Warning!"))
        self.label.setAccessibleName(_translate("Error", "errmsg"))
        self.label.setText(_translate("Error", "에러 메시지"))
        self.pushButton.setAccessibleName(_translate("Error", "okay_button"))
        self.pushButton.setText(_translate("Error", "확인"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Error = QtWidgets.QDialog()
    ui = view_ErrorMsg()
    ui.setupUi(Error)
    Error.show()
    sys.exit(app.exec_())