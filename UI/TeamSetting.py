from PyQt5 import QtCore, QtGui, QtWidgets
from UI import ErrorMessage

'''
- 최초작성자 : 이영찬
- 최초작성일 : 2018.11.29
- 최초변경일 : 2018.12.06
- 목적 : 교수의 팀 조건 설정 인터페이스
- 개정이력 : 이영찬, 2018.12.06 
'''

class view_TeamSetting(object):
    def __init__(self, prof):
        self.__dialog = None
        self.owner = prof

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

        self.__dialog = Dialog
        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(self.okayButtonClicked)
        self.pushButton_2.clicked.connect(self.__dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    #목적 : 확인 버튼 클릭 시 입력된 값으로 팀 구성 인원을 설정한다.
    def okayButtonClicked(self):
        print("확인 버튼")
        limit = self.spinBox.text()
        print(limit)
        if int(limit) <= 0 :
            dialog = QtWidgets.QDialog()
            ui = ErrorMessage.view_ErrorMsg()
            ui.setupUi(dialog)
            ui.label.setText("팀 인원 제한을 1명 이상으로 해 주십시오.")
            dialog.exec()
        else:
            self.owner.setLimit(int(limit))
            self.__dialog.close()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "TeamSetting"))
        self.spinBox.setAccessibleName(_translate("Dialog", "limitnum"))
        self.label.setText(_translate("Dialog", "인원설정"))
        self.pushButton.setText(_translate("Dialog", "확인"))
        self.pushButton_2.setText(_translate("Dialog", "취소"))

if __name__ == "__main__":
    import sys
    import os

    mypath = os.path.dirname(sys.executable) + "\Lib\site-packages\PyQt5\Qt\plugins"
    libpaths = QtWidgets.QApplication.libraryPaths()
    libpaths.append(mypath)
    QtWidgets.QApplication.setLibraryPaths(libpaths)

    app = QtWidgets.QApplication(sys.argv)
    Dialogs = QtWidgets.QDialog()
    ui = view_TeamSetting('a')
    ui.setupUi(Dialogs)
    Dialogs.show()
    sys.exit(app.exec_())

