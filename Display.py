from UI import login, studModInfo, studMainWindow, ErrorMessage, Message,\
    profMakeBang, profModeInfo, profAddInfo, profEnterBang, profMainWindow,\
    TeamSetting
import sys
import os
from PyQt5 import QtWidgets

mypath = os.path.dirname(sys.executable) + "\Lib\site-packages\PyQt5\Qt\plugins"
libpaths = QtWidgets.QApplication.libraryPaths()
libpaths.append(mypath)
QtWidgets.QApplication.setLibraryPaths(libpaths)

class Display:
    Dialog = None
    ui = None
    login = None
    studMod = None
    studMain =None
    error = None
    message = None
    profBang = None
    profMain = None
    profMod = None
    profAdd = None
    makeBang = None
    teamSet = None

    me = None

    def __init__(self, client):
        self.bangList = []
        self.bangIndex = []
        self.login = login.view_Login(client)

    def giveRef(self, whoRU, role):
        self.me = whoRU
        self.role = role

    def getMyStdList(self):
        return self.stdList

    def messageSend(self, message, froms):
        print("message is ", message)

    def openView(self, name):
        if name == "LogIn":
            self.Dialog = QtWidgets.QDialog()
            self.ui = self.login
            self.ui.setupUi(self.Dialog)
            self.Dialog.show()

        elif name == "StudMain":
            if self.studMain == None:
                self.studMain = studMainWindow.view_studMainWindow(self.stdList,self.me,self.switch)
                self.Main = QtWidgets.QMainWindow()
            else:
                self.studMain.updateList(self.stdList,self.switch)
            self.ui = self.studMain
            self.ui.setupUi(self.Main)
            self.Main.show()
        elif name == "ProfBangList":
            if self.profBang == None:
                self.profBang = profEnterBang.view_EnterBang(self.bangList,self.bangIndex,self.me)
                self.Dialog = QtWidgets.QDialog()
            else:
                self.profBang.updateList(self.bangList, self.bangIndex)
                self.Dialog = QtWidgets.QDialog()
            self.ui = self.profBang
            self.ui.setupUi(self.Dialog)
            self.Dialog.show()
        elif name == "ProfMain":
            if self.profMain == None:
                self.profMain = profMainWindow.view_ProfMainWindow(self.stdList, self.me, self.switch)
                self.Main = QtWidgets.QMainWindow()
            else:
                self.profMain.updateList(self.stdList,self.switch)
            self.ui = self.profMain
            self.ui.setupUi(self.Main)
            self.Main.show()

    #def refreshView(self,):

    def closeView(self, name):
        if name == "Login":
            self.ui.close_view()

    def refreshBangList(self, bangList, bangIndex):
        self.bangList = bangList
        self.bangIndex = bangIndex
        self.openView("ProfBangList")

    def refreshBang(self, student, switchStat):
        self.stdList = student
        self.switch = switchStat
        if self.role == "Student":
            self.openView("StudMain")
        else:
            self.openView("ProfMain")

    def getDisplayOwnerID(self):
        print("message is ")
    def __refreshView(self, view):
        print("message is ")
