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
    bangList = []
    bangIndex = []
    me = None

    def __init__(self, client):
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
            ...
        elif name == "ProfBangList":
            if self.profBang == None:
                self.profBang = profEnterBang.view_EnterBang(self.bangList,self.bangIndex,self.me)
            self.Dialog = QtWidgets.QDialog()
            self.ui = self.profBang
            self.ui.setupUi(self.Dialog)
            self.Dialog.show()
        elif name == "ProfMain":
            if self.profMain == None:
                self.profMain = profMainWindow.view_ProfMainWindow(self.stdList, self.switch, self.me)
            self.Dialog = QtWidgets.QDialog()
            self.ui = self.profMain
            self.ui.setupUi(self.Dialog)
            self.Dialog.show()

    def closeView(self, name):
        if name == "Login":
            self.ui.close_view()

    def refreshBangList(self, bangList, bangIndex):
        self.bangList = bangList
        self.bangIndex = bangIndex

    def refreshBang(self, student, switchStat):
        self.stdList = student
        self.switch = switchStat

    def getDisplayOwnerID(self):
        print("message is ")
    def __refreshView(self, view):
        print("message is ")
