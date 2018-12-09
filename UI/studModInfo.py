from PyQt5 import QtCore, QtGui, QtWidgets
from UI import ErrorMessage
'''
- 최초작성자 : 이영찬
- 최초작성일 : 2018.11.29
- 최초변경일 : 2018.12.06
- 목적 : 학생의 정보 수정 인터페이스
- 개정이력 : 이영찬, 2018.12.06
'''

class view_studModInfo(object):
    def __init__(self, stud):
        self.__dialog = None
        self.owner = stud

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(413, 303)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 220, 391, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("확인")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("취소")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 80, 47, 121))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어라운드 ExtraBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어라운드 ExtraBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(80, 60, 321, 151))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit.setObjectName("이름 입력 란")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_2.setObjectName("연락처 입력 란")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 371, 41))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어라운드 ExtraBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.__dialog = Dialog
        self.retranslateUi(Dialog)
        #확인버튼 클릭 시 학생의 정보 수정 함수를 호출
        self.pushButton.clicked.connect(self.okayButtonClicked)
        self.pushButton_2.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    #목적 : 확인 버튼 클릭 시 입력 된 정보를 바탕으로 정보를 수정하는 메서드를 호출
    def okayButtonClicked(self):
        print("확인 버튼")
        if self.lineEdit.text() == "" or self.lineEdit_2.text() == "":
            dialog = QtWidgets.QDialog()
            ui = ErrorMessage.view_ErrorMsg()
            ui.setupUi(dialog)
            ui.label.setText("수정 정보를 모두 입력해주시기 바랍니다")
            dialog.exec()
        else:
            name = self.lineEdit.text()
            phoneNo = self.lineEdit_2.text()
            self.owner.modMyInform(name, phoneNo)
            self.__dialog.close()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Information Mod"))
        self.pushButton.setAccessibleName(_translate("Dialog", "okay_Button"))
        self.pushButton.setText(_translate("Dialog", "확인"))
        self.pushButton_2.setAccessibleName(_translate("Dialog", "cancel_Button"))
        self.pushButton_2.setText(_translate("Dialog", "취소"))
        self.label_2.setText(_translate("Dialog", "이름"))
        self.label_3.setText(_translate("Dialog", "연락처"))
        self.lineEdit.setAccessibleName(_translate("Dialog", "studName"))
        self.lineEdit_2.setAccessibleName(_translate("Dialog", "phoneNo"))
        self.label.setText(_translate("Dialog", "수정할 정보"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialogs = QtWidgets.QDialog()
    ui = view_studModInfo()
    ui.setupUi(Dialogs)
    Dialogs.show()
    sys.exit(app.exec_())

