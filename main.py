import Client
import InitializeManager
import os
import sys
from PyQt5 import QtWidgets

class MainWindow(QtWidgets.QWidget):
    def __init__(self, main, parent=None):
        super().__init__()
        self.setGeometry(50, 50, 400, 450)
        self.setFixedSize(400, 450)
        main.main()

class Main:
    def __init__(self):
        ...
    def main(self):
        initial = InitializeManager.InitializeManager("Professor List.txt")
        client = Client.Client(initial)

if __name__ == '__main__':

    mypath = os.path.dirname(sys.executable) + "\Lib\site-packages\PyQt5\Qt\plugins"
    libpaths = QtWidgets.QApplication.libraryPaths()
    libpaths.append(mypath)
    QtWidgets.QApplication.setLibraryPaths(libpaths)

    app = QtWidgets.QApplication(sys.argv)
    mains = Main()
    MW = MainWindow(mains)
    MW.show()
    sys.exit(app.exec_())