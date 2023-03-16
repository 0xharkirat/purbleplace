import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui import Ui_MainWindow


class ZoomBotUI(QMainWindow):
    def __init__(self):
        super(ZoomBotUI,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = ZoomBotUI()
    sys.exit(app.exec_())
