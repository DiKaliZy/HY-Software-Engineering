import UI.ErrorMessage
import Client

class Display:
    def __init__(self, client):
        #test
        self.client = client

    def giveRef(self, whoRU):
        self.userref = whoRU

    def messageSend(self, message, froms):
        print("message is ", message)

    def openView(self, name):
        if name == "LogIn":
            print("login!")
            #test용
            self.client.logIn("204111", "우헹헹", -1)

    def refreshBangList(self, bangList, bangIndex):
        print("message is ")
    def refreshBang(self, student, switchStat):
        print("message is ")
    def getDisplayOwnerID(self):
        print("message is ")
    def __refreshView(self, view):
        print("message is ")