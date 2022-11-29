from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QToolButton, QApplication
from PyQt5.QtCore import QCoreApplication

from questions import examList

from testscore import TestScore

class MidTermTest(QWidget):

    def buttonClicked(self):
        for i in range(self.questionsNumber):
            userInput = self.answerInputs[i].text()
            if userInput == self.examPaper[self.examQuestionList[i]]:
                TestScore.score += 1
        print(TestScore.score)
        QCoreApplication.instance().quit()



    def __init__(self, difficulty, parent=None):
        super().__init__(parent)
        self.examPaper = examList[difficulty]
        self.examQuestionList = list(self.examPaper.keys())
        self.questionsNumber = len(self.examPaper)
        examLayout = QGridLayout()

        self.examQuestionLabels = [QLabel() for _ in range(self.questionsNumber)]
        for i in range(3):
            self.examQuestionLabels[i].setText(self.examQuestionList[i])

        r = 0
        c = 0
        for question in self.examQuestionLabels:
            examLayout.addWidget(question, r, 0)
            r += 1

        self.answerInputs = [QLineEdit() for _ in range(self.questionsNumber)]
        for answer in self.answerInputs:
            examLayout.addWidget(answer, c, 1)
            c += 1

        self.submitButton = QToolButton()
        self.submitButton.setText("Submit!")
        self.submitButton.clicked.connect(self.buttonClicked)
        examLayout.addWidget(self.submitButton, 3, 0)

        self.setLayout(examLayout)
        self.setWindowTitle('MidTerm Test')


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    test = MidTermTest(0)
    test.show()
    sys.exit(app.exec_())
