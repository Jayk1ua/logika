from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from random import randint


app = QApplication([])
main_window = QWidget()

button = QPushButton('Згенерувати!')
text = QLabel('Натисни, щоб дізнатись переможця')
winner = QLabel('?')

line = QVBoxLayout()
line.addWidget(text, alignment=Qt.AlignCenter)
line.addWidget(winner, alignment=Qt.AlignCenter)
line.addWidget(button, alignment=Qt.AlignCenter)




def win():
    ran = randint(1, 100)
    winner.setText(str(ran))
    text.setText('Переможець')
    button.hide()

button.clicked.connect(win)

main_window.setLayout(line)
main_window.show()
app.exec_()