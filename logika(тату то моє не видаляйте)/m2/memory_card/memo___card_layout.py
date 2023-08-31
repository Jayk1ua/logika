''' Вікно для картки питання '''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QTableWidget, QListWidget, QListWidgetItem,
        QLineEdit, QFormLayout,
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QSpinBox)
app = QApplication([])


btn_menu = QPushButton('Меню')

btn_sleep = QPushButton('Відпочити')
btn_ok = QPushButton('Відповісти')
lb_question = QLabel('')

box_minutes = QSpinBox()
box_minutes.setValue(5)

RadioGroupBox = QGroupBox('Варіанти відповідей')
RadioGroup = QButtonGroup()
rbtn1 = QRadioButton('')
rbtn2 = QRadioButton('')
rbtn3 = QRadioButton('')
rbtn4 = QRadioButton('')

RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn1)
layout_ans2.addWidget(rbtn2)
layout_ans3.addWidget(rbtn3)
layout_ans3.addWidget(rbtn4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupbox = QGroupBox('Результат тесту')
lb_result = QLabel('')
lb_correct = QLabel('')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_correct, alignment=Qt.AlignHCenter)
AnsGroupbox.setLayout(layout_res)
AnsGroupbox.hide()

Layout_line1 = QHBoxLayout()
Layout_line2 = QHBoxLayout()
Layout_line3 = QHBoxLayout()
Layout_line4 = QHBoxLayout()

Layout_line1.addWidget(btn_menu)
Layout_line1.addStretch(1)
Layout_line1.addWidget(btn_sleep)
Layout_line1.addWidget(box_minutes)
Layout_line1.addWidget(QLabel('Хвилин'))

Layout_line2.addWidget(lb_question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

Layout_line3.addWidget(RadioGroupBox)
Layout_line3.addWidget(AnsGroupbox)

Layout_line4.addStretch(1)
Layout_line4.addWidget(btn_ok)
Layout_line4.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(Layout_line1)
layout_card.addLayout(Layout_line2)
layout_card.addLayout(Layout_line3)
layout_card.addLayout(Layout_line4)



def show_result():
    ''' показати панель відповідей '''
    pass

def show_question():
    ''' показати панель запитань '''
    pass