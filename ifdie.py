from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QToolButton, QApplication
from PyQt5.QtCore import QCoreApplication
import sys




class ifdie(QWidget):


    def rebuttonClicked(self):
        QCoreApplication.instance().quit()

    def quitbuttonClicked(self):
        sys.exit(0)

    def __init__(self, parent = None):
        super().__init__(parent)


        btLayout = QGridLayout()
        self.reButton = QToolButton()
        self.reButton.setText("재시작하기")
        self.quitButton= QToolButton()
        self.quitButton.setText("나가기")
        self.exlabel = QLabel("이런!! 쿠민이의 인생이 종료되었습니다.",self)
        font1 = self.exlabel.font()
        font1.setPointSize(15)
        font1.setBold(True)
        self.exlabel.setFont(font1)
        self.reButton.clicked.connect(self.rebuttonClicked)
        self.quitButton.clicked.connect(self.quitbuttonClicked)
        btLayout.addWidget(self.exlabel,0,0)
        btLayout.addWidget(self.reButton,1,0)
        btLayout.addWidget(self.quitButton,1,1)

        self.setLayout(btLayout)
        self.setWindowTitle("Re: or Quit")

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    setting = ifdie()
    setting.show()
    sys.exit(app.exec_())