from PyQt5 import QtCore, QtGui, QtWidgets
'''
최초작성자 : 이영찬
최초작성일 : 2018.11.29
최초변경일 :
목적 : 교수의 학생 추가시 제공할 인터페이스 구현
개정 이력 :
'''
class view_profAddInfo(object):
    def __init__(self, prof):
        self. owner = prof

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(401, 306)
        Dialog.setToolTipDuration(0)
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
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어라운드 ExtraBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어라운드 ExtraBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_2.addWidget(self.lineEdit_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        id = self.lineEdit.text()
        name = self.lineEdit_2.text()
        phoneNo = self.lineEdit_3.text()

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(self.okayButtonClicked(id, name, phoneNo))
        self.pushButton_2.clicked.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    # 목적 : 확인버튼 클릭 시 학생을 추가하는 메서드 호출
    def okayButtonClicked(self, id, name, phoneNo):
        # 학번 혹은 이름 미입력시 에러메시지 출력
        if id == None or name == None or phoneNo == None:
            window = view_Errormsg()
            window.setMessage("정보를 모두 입력해주십시오")
            window.exec_()
        else:
            self.owner.inputStud(id, name, phoneNo)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "학생정보추가"))
        self.pushButton.setText(_translate("Dialog", "확인"))
        self.pushButton_2.setText(_translate("Dialog", "취소"))
        self.label.setText(_translate("Dialog", "학번"))
        self.label_2.setText(_translate("Dialog", "이름"))
        self.label_3.setText(_translate("Dialog", "연락처"))
        self.lineEdit.setAccessibleName(_translate("Dialog", "StudNo"))
        self.lineEdit_2.setAccessibleName(_translate("Dialog", "studName"))
        self.lineEdit_3.setAccessibleName(_translate("Dialog", "phoneNo"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = view_profAddInfo()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

