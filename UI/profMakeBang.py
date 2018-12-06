# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'profMakeBang.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class view_makebang(object):
    def setupUi(self, Software_Engineering):
        Software_Engineering.setObjectName("Software_Engineering")
        Software_Engineering.resize(400, 296)
        self.pushButton_3 = QtWidgets.QPushButton(Software_Engineering)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 170, 121, 31))
        self.pushButton_3.setObjectName("찾아보기")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Software_Engineering)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 210, 391, 80))
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
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Software_Engineering)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(140, 70, 251, 101))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit.setObjectName("과목명 작성")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_2.setObjectName("명단파일 주소")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayoutWidget = QtWidgets.QWidget(Software_Engineering)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 125, 151))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어라운드 ExtraBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어라운드 ExtraBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어라운드 ExtraBold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)

        file = self.lineEdit_2.text()
        name = self.lineEdit.text()

        self.retranslateUi(Software_Engineering)
        self.pushButton.clicked.connect(Professor.makeBang(file, name))
        self.pushButton_2.clicked.connect(Software_Engineering.reject)
        self.pushButton_3.clicked.connect(self.findButtonClicked)
        QtCore.QMetaObject.connectSlotsByName(Software_Engineering)

    #목적 : 방 DB 파일 path를 가져옴
    def findButtonClicked(self):
        fname = QFileDialog.getOpenFileName(self)
        self.lineEdit_2.setText(fname[0])

    def retranslateUi(self, Software_Engineering):
        _translate = QtCore.QCoreApplication.translate
        Software_Engineering.setWindowTitle(_translate("Software_Engineering", "makeBang"))
        self.pushButton_3.setAccessibleName(_translate("Software_Engineering", "upload_button"))
        self.pushButton_3.setText(_translate("Software_Engineering", "찾아보기"))
        self.pushButton.setAccessibleName(_translate("Software_Engineering", "okay_button"))
        self.pushButton.setText(_translate("Software_Engineering", "확인"))
        self.pushButton_2.setAccessibleName(_translate("Software_Engineering", "cancel_button"))
        self.pushButton_2.setText(_translate("Software_Engineering", "취소"))
        self.lineEdit_2.setAccessibleName(_translate("Software_Engineering", "className"))
        self.lineEdit.setAccessibleName(_translate("Software_Engineering", "classFile"))
        self.label.setText(_translate("Software_Engineering", "방 생성"))
        self.label_2.setText(_translate("Software_Engineering", "과목명"))
        self.label_3.setText(_translate("Software_Engineering", "명단파일"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    makebang = QtWidgets.QDialog()
    ui = view_makebang()
    ui.setupUi(makebang)
    makebang.show()
    sys.exit(app.exec_())
