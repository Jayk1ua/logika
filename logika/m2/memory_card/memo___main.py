from memo___card_layout import *
from PyQt5.QtWidgets import QWidget, QApplication
from random import shuffle # будемо змішувати відповіді в картці питання
from memo___data import *
card_width, card_height = 600, 500 # початкові розміри вікна "картка"


radio_list = [rbtn1, rbtn2, rbtn3, rbtn4]
 
frm = Question('Яблоко','apple','cadle','sunny','sunshine')
frm_card = QuestionView(frm, lb_question, radio_list[0], radio_list[1], radio_list[2], radio_list[3])


def show_data():
    ''' показує на екрані потрібну інформацію '''
    pass

def check_result():
    ''' перевірка, чи вибрана правильна відповідь 
    якщо відповідь була вибрана, то напис "правильно/не правильно" отримує потрібне значення
    і показує панель відповідів'''
    pass

win_card = QWidget()
win_card.resize(card_width, card_height)

frm_card.show()
#тут повинні бути параметри вікна
win_card.setLayout(layout_card)
win_card.show()
app.exec_()