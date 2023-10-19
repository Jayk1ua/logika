#Імпорти
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, 
    QHBoxLayout, QVBoxLayout, QListWidget, QLineEdit, 
    QTextEdit, QInputDialog, QTableWidget,  QListWidgetItem,
    QFormLayout, QGroupBox, QButtonGroup, QRadioButton, QSpinBox, QFileDialog)
from PyQt5.QtGui import QPixmap 
import json 


from PIL import Image, ImageFilter

import os


app = QApplication([])
window = QWidget()
window.setStyleSheet('''
                        background-color: black;
                        color: yellow;
                        font-size: 20px;
                        border: 2px solid purple; 
                        ''')

#Кнопки
btn_folder = QPushButton('Папка')
btn_left = QPushButton('Вліво')
btn_right = QPushButton('Вправо')
btn_mirror = QPushButton('Дзеркало')
btn_sharpness = QPushButton('Різкість')
btn_bw = QPushButton('Ч/Б')

listpicture = QListWidget()
picture = QLabel('Картинка')

#Лінії
layout_editor = QHBoxLayout()

col1 = QVBoxLayout()
col2 = QVBoxLayout()

row = QHBoxLayout()
#Додавання кнопок+ліній
col1.addWidget(btn_folder)
col1.addWidget(listpicture)

row.addWidget(btn_left)
row.addWidget(btn_right)
row.addWidget(btn_mirror)
row.addWidget(btn_sharpness)
row.addWidget(btn_bw)

col2.addWidget(picture)
col2.addLayout(row)

layout_editor.addLayout(col1, 1)
layout_editor.addLayout(col2, 4)

#workdir = 'D:\\Ярлики\\logika(тату то моє не видаляйте)\\m4\\y1\\eazyeditor'
workdir = QFileDialog.getExistingDirectory()



files = os.listdir(workdir)



def filter(filenames):
    result = []
    ext = ['jpg', 'png', 'jpeg', 'bmp', 'gif']


    for file in filenames:
        if file.split('.')[-1] in ext:
            result.append(file)

filter(files)





window.setLayout(layout_editor)
window.show()
app.exec_()