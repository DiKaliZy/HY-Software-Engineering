from PyQt5 import QtCore, QtGui, QtWidgets
from UI import ErrorMessage
'''
- 최초작성자 : 이영찬
- 최초작성일 : 2018.11.29
- 최초변경일 : 2018.12.06
- 목적 : 교수의 학생 정보 수정
- 개정이력 : 이영찬, 2018.12.06
'''

class view_profModInfo(object):
    def __init__(self, prof):
        self.owner = prof
        self.__dialog = Dialog

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 220, 371, 80))
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
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 371, 200))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어라운드 ExtraBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("학번")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어라운드 ExtraBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("이름")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어라운드 ExtraBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("연락처")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어라운드 ExtraBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("팀번호")
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit.setObjectName("학번 입력")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_2.setObjectName("이름 입력")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_3.setObjectName("연락처 입력")
        self.verticalLayout_2.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_4.setObjectName("팀번호 입력")
        self.verticalLayout_2.addWidget(self.lineEdit_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.retranslateUi(Dialog)
        #확인 버튼 클릭 시 정보수정 함수 호출
        self.pushButton.clicked.connect(self.okayButtonClicked)
        self.pushButton_2.clicked.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    #목적 : 확인 버튼 클릭 시 입력된 정보를 바탕으로 정보 수정 메서드를 호출한다.
    def okayButtonClicked(self):
        print("확인 버튼")
        id = int(self.lineEdit.text())
        name = self.lineEdit_2.text()
        phoneNo = int(self.lineEdit_3.text())
        teamNo = int(self.lineEdit_4.text())

        if id == None or name == None or phoneNo == None or teamNo == None :
            dialog = QtWidgets.QDialog()
            ui = ErrorMessage.view_ErrorMsg()
            ui.setupUi(dialog)
            ui.label.setText("수정 정보를 모두 입력해주시기 바랍니다")
            dialog.show()
        else:
            self.owner.modStudInform(id, name, phoneNo, teamNo)
        self.__dialog.close()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "ProfModInfo"))
        self.pushButton.setText(_translate("Dialog", "확인"))
        self.pushButton_2.setText(_translate("Dialog", "취소"))
        self.label.setText(_translate("Dialog", "학번"))
        self.label_2.setText(_translate("Dialog", "이름"))
        self.label_3.setText(_translate("Dialog", "연락처"))
        self.label_4.setText(_translate("Dialog", "팀번호"))
        self.lineEdit.setAccessibleName(_translate("Dialog", "StudNo"))
        self.lineEdit_2.setAccessibleName(_translate("Dialog", "studName"))
        self.lineEdit_3.setAccessibleName(_translate("Dialog", "phoneNo"))
        self.lineEdit_4.setAccessibleName(_translate("Dialog", "teamNo"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = view_profModInfo()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

