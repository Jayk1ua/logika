from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout, QRadioButton, QMessageBox


app = QApplication([])
window = QWidget()

text = QLabel('Коли випустили доту?')
ans1 = QRadioButton("09.07.2013")
ans2 = QRadioButton("13.03.2017")
ans3 = QRadioButton('27.05.2007')
ans4 = QRadioButton('28.08.2014')


vline = QVBoxLayout()
hline1 = QHBoxLayout()
hline2 = QHBoxLayout()
hline3 = QHBoxLayout()

hline1.addWidget(text, alignment=Qt.AlignCenter)
hline2.addWidget(ans1, alignment=Qt.AlignCenter)
hline2.addWidget(ans2, alignment=Qt.AlignCenter)
hline3.addWidget(ans3, alignment=Qt.AlignCenter)
hline3.addWidget(ans4, alignment=Qt.AlignCenter)
vline.addLayout(hline1)
vline.addLayout(hline2)
vline.addLayout(hline3)

def win():
    window2 = QMessageBox()
    window2.setText('Правильно')
    window2.exec_()

def lose():
    window3 = QMessageBox()
    window3.setText('Неправильно')
    window3.exec_()
    

ans1.clicked.connect(win)
ans2.clicked.connect(lose)
ans3.clicked.connect(lose)
ans4.clicked.connect(lose)


window.setLayout(vline)
window.show()
app.exec_()