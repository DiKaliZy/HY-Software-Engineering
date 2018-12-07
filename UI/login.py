from PyQt5 import QtCore, QtGui, QtWidgets
'''
최초작성자 : 이영찬
최초작성일 : 2018.11.29
최초변경일 :
목적 : 로그인 화면 생성
개정 이력 :
'''
class view_Login(object):
    def __init__(self):
        self.__dialog = None

    def setupUi(self, Dialog):
        self.__dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(413, 303)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 220, 391, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("Okay")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("Cancel")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 58, 161))
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
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어라운드 ExtraBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(80, 20, 321, 181))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_2.addWidget(self.lineEdit_3)

        name = self.lineEdit.text()
        id = self.lineEdit_2.text()
        bangNo = self.lineEdit_3.text()

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(self.okayButtonClicked(name, id, bangNo))
        self.pushButton_2.clicked.connect(self.cancelButtonClicked)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    #목적 : 확인 버튼 클릭 시 클라이언트의 login 메서드 호출
    #매개변수 : 이름, 연락처, 방번호
    def okayButtonClicked(self, name, id, bangNo):
        if bangNo == None:
            setbangNo = -1
            #client.login(name, id, setbangNo)
        else:
            print(name, id, bangNo)
            #client.login(name, id, bangNo)
        self.__dialog.close()
    #목적 : 취소 버튼 클릭 시 창 닫기(프로그램 종료)
    #매개변수 : 없음
    def cancelButtonClicked(self):
        self.__dialog.close()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Login_Window"))
        self.pushButton.setText(_translate("Dialog", "확인"))
        self.pushButton_2.setText(_translate("Dialog", "취소"))
        self.label_2.setText(_translate("Dialog", "이름"))
        self.label_3.setText(_translate("Dialog", "학번"))
        self.label.setText(_translate("Dialog", "방 번호"))
        self.lineEdit.setAccessibleName(_translate("Dialog", "name"))
        self.lineEdit_2.setAccessibleName(_translate("Dialog", "PhoneNo"))
        self.lineEdit_3.setAccessibleName(_translate("Dialog", "BangNo"))

    def show(self):
        ui = view_Login
        ui.setupUi(Dialog)
        Dialog.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = view_Login()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

