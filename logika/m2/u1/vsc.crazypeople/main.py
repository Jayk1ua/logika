from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel

app = QApplication([])
main_window = QWidget()

button = QPushButton('Натисни!')
text = QLabel('Натисни, щоб дізнатись переможця')
winner = QLabel('?')

line = QVBoxLayout()
line.addWidget(text)
line.addWidget(winner)
line.addWidget(button)

main_window.setLayout(line)
main_window.show()
app.exec_()