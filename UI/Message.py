from PyQt5 import QtCore, QtGui, QtWidgets
'''
최초작성자 : 이영찬
최초작성일 : 2018.11.29
최초변경일 :
목적 : 메시지 생성화면 출력
개정 이력 :
'''

class view_Message(object):
    def __init__(self, stud, display):
        self.__dialog = None
        self.owner = stud
        self.dis = display

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
        self.__dialog=Dialog

        #name, code, to = display.

        # 승락 버튼 클릭 시 positive 메서드 호출
        self.pushButton.clicked.connect(self.posClicked)
        # 거절 버튼 클릭 시 negative 메서드 호출
        self.pushButton_2.clicked.connect(self.negClicked)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    #목적 : 승락버튼을 클릭 시 승락 메서드를 호출한다.
    def posClicked(self):
        to = self.owner
        self.owner.positive(to)

    #목적 : 거절버튼을 클릭 시 거절 메서드를 호출한다.
    def negClicked(self):
        to = self.owner
        self.owner.negative(to)

    #목적 : 외부에서 메시지를 사용하고자 할 때 메시지의 내용을 설정한다.
    def setMessage(self, context):
        self.label.setText(context)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Message"))
        self.label.setAccessibleName(_translate("Dialog", "JoinMessage"))
        self.label.setText(_translate("Dialog", " "))
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

