#Імпорти
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, 
    QHBoxLayout, QVBoxLayout, QListWidget, QLineEdit, 
    QTextEdit, QInputDialog, QTableWidget,  QListWidgetItem,
    QFormLayout, QGroupBox, QButtonGroup, QRadioButton, QSpinBox)
import json 

def writeToFile():
    with open('notes.json', 'w', encoding='utf-8') as file:
        json.dump(notes, file, ensure_ascii=False, sort_keys=True, indent=4)


#Вікно
app = QApplication([])
window = QWidget()



#Кнопки
field_text = QTextEdit()
lb_notes = QLabel('Список заміток')
lst_notes = QListWidget()


btn_add_notes = QPushButton('Створити замітку')
btn_del_notes = QPushButton('Видалити замітку')
btn_save_notes = QPushButton('Зберегти замітку')

lb_tags = QLabel('Список тегів')
lst_tags = QListWidget()


btn_tag_add = QPushButton('Додати тег')
btn_tag_unpin = QPushButton('Відкріпити від замітки')
btn_tag_search = QPushButton('Шукати за тегом')
btn_tag_searchfor = QLineEdit()


#Лінії + додавання віджетів
layout_notes = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()

layout_notes.addLayout(col1, stretch=2)
layout_notes.addLayout(col2, stretch=1)

col1.addWidget(field_text)

col2.addWidget(lb_notes)
col2.addWidget(lst_notes)

row1 = QHBoxLayout()
row1.addWidget(btn_add_notes)
row1.addWidget(btn_del_notes)

col2.addLayout(row1)
col2.addWidget(btn_save_notes)
col2.addWidget(lb_tags)
col2.addWidget(lst_tags)

col2.addWidget(btn_tag_searchfor)

row2 = QHBoxLayout()
row2.addWidget(btn_tag_add)
row2.addWidget(btn_tag_unpin)

col2.addLayout(row2)
col2.addWidget(btn_tag_search)

window.setLayout(layout_notes)




#Відкриття файлу в json
with open('notes.json', 'r', encoding='utf-8') as file:
    notes = json.load(file)



#функція, щоб дістати текст
def show_note():
    key = lst_notes.currentItem().text()

    field_text.setText(notes[key]['текст'])

    lst_tags.clear()
    lst_tags.addItems(notes[key]['теги'])


#Програмування кнопок
def add_note():
    note_name, ok = QInputDialog.getText(window, 'Додати замітку', 'Назва замітки')

    if note_name and ok:
        notes[note_name] = {'текст': '', 'теги': []}
        lst_notes.addItem(note_name)


def save_note():
    if lst_notes.currentItem():
        key = lst_notes.currentItem().text()
        notes[key]['текст'] = field_text.toPlainText()
        writeToFile()


def del_note():
    if lst_notes.currentItem():
        key  = lst_notes.currentItem().text()
        del notes[key]

        field_text.clear()
        lst_tags.clear()
        lst_notes.clear()

        lst_notes.additems(notes)
        writeToFile()


#!!!
lst_notes.itemClicked.connect(show_note)

btn_add_notes.clicked.connect(add_note)
btn_save_notes.clicked.connect(save_note)
btn_del_notes.clicked.connect(del_note)
lst_notes.addItems(notes)

#Показ
window.show()
app.exec_()