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

#програма
app = QApplication([])
window = QWidget()
window.setStyleSheet('''
                        background-color: black;
                        color: yellow;
                        font-size: 20px;
                        border: 2px solid yellow; 
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







#фільтер файлів

def filter(filenames):
    result = []
    ext = ['jpg', 'png', 'jpeg', 'bmp', 'gif']


    for file in filenames:
        if file.split('.')[-1] in ext:
            result.append(file)
    return result



def showfilenamelist():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
    files = os.listdir(workdir)
    filtered_img = filter(files)

    listpicture.clear()

    listpicture.addItems(filtered_img)



#Клас
class ImageProcessor():
    def __init__(self):
        self.original = None
        self.filename = None
        self.save_dir = 'modified/'

    def LoadImage(self, filename):
        self.filename = filename

        full_path = os.path.join(workdir, filename)

        self.original = Image.open(full_path)

    
    def show_image(self, path):
        picture.hide()

        pixmapimage = QPixmap(path)

        w, h  = picture.width(), picture.height()

        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        picture.setPixmap(pixmapimage)


        picture.show()
    

    def saveAndShowImage(self):
        path = os.path.join(workdir, self.save_dir)
        

        if not (os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)

        image_path = os.path.join(path, self.filename)
        self.original.save(image_path)
        self.show_image(image_path)



    def do_bw(self):
        self.original = self.original.convert('L')
        self.saveAndShowImage()

    def do_left(self):
        self.original = self.original.transpose(Image.ROTATE_90)
        self.saveAndShowImage()

    def do_right(self):
        self.original = self.original.transpose(Image.ROTATE_270)
        self.saveAndShowImage()


    def flip(self):
        self.original = self.original.transpose(Image.FLIP_LEFT_RIGHT)
        self.saveAndShowImage()


    def do_sharp(self):
        self.original = self.original.filter(ImageFilter.SHARPEN)
        self.saveAndShowImage()


#Показ вибраного фото
def showChosenItem():
    filename = listpicture.currentItem().text()
    work_image.LoadImage(filename)
    full_path = os.path.join(workdir, filename)
    work_image.show_image(full_path)

work_image = ImageProcessor()

#Під'єднання
listpicture.itemClicked.connect(showChosenItem)

btn_folder.clicked.connect(showfilenamelist)

btn_bw.clicked.connect(work_image.do_bw)

btn_left.clicked.connect(work_image.do_left)

btn_right.clicked.connect(work_image.do_right)

btn_mirror.clicked.connect(work_image.flip)

btn_sharpness.clicked.connect(work_image.do_sharp)


#Показ
window.resize(900,600)
window.setLayout(layout_editor)
window.show()
app.exec_()