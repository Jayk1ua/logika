from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel

app = QApplication([])
main_window = QWidget()

button = QPushButton('Натисни!')
text = QLabel('Натисни . . . .')
winner = QLabel('?')

main_window.show()
app.exec_()