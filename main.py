# main.py

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QDialog, QDialogButtonBox, \
    QVBoxLayout, QWidget
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

import test
from objects import Answer, Question, TestEndData
from test import create_test, getResults
import faulthandler

faulthandler.enable()

class PersonalityTestApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('interface.ui', self)

        # Set up UI elements
        self.questionLabel = self.findChild(QLabel, 'questionLabel')
        self.imageLabel = self.findChild(QLabel, 'imageLabel')
        self.answersLayout = self.findChild(QWidget, 'verticalLayoutWidget').layout()

        # Define the test questions
        self.test = create_test()
        self.current_question = self.test[0]

        # Display the first question
        self.display_question(self.current_question)

    def display_question(self, question):
        self.questionLabel.setText(question.title)
        self.imageLabel.setPixmap(QPixmap(question.image))

        # Clear previous answer buttons
        while self.answersLayout.count():
            child = self.answersLayout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        for answer in question.answers:
            btn = QPushButton(answer.text, self)
            btn.clicked.connect(lambda _, a=answer: self.on_answer(a))
            self.answersLayout.addWidget(btn)

    def on_answer(self, answer):
        if answer.on_answer:
            answer.on_answer()
        if answer.next_question:
            self.display_question(answer.next_question)
        else:
            self.show_results_dialog()

    def show_results_dialog(self):
        results = getResults()
        dialog = QDialog(self)
        uic.loadUi('testEndDialog.ui', dialog)

        dialog.imageLabel.setPixmap(QPixmap(results.image))
        dialog.titleLabel.setText(results.title)
        dialog.descLabel.setText(results.desc)

        dialog.accepted.connect(self.reset_test)  # Connect reset_test to dialog accepted signal
        dialog.rejected.connect(self.reset_test)

        dialog.exec_()

    def reset_test(self):
        test.initialize_scores()
        self.current_question = self.test[0]
        self.display_question(self.current_question)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PersonalityTestApp()
    window.show()
    sys.exit(app.exec_())
