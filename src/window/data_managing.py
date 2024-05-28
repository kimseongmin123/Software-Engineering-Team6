import json

import sys
from PyQt6.QtWidgets import *
from PyQt6 import uic

sys.path.append('.')

import pandas as pd
from src.module.data_processing import *

df = pd.read_csv('data/hackers_test/hackers_test_raw.csv', encoding='cp949')

df.drop(['Day', 'Unnamed: 4', 'Unnamed: 5', '외움'], axis=1, inplace=True)

df['뜻'] = df['뜻'].apply(remove_parentheses).apply(remove_comma).apply(remove_semicolon).apply(remove_whitespace)
df = df[~df['뜻'].str.contains('~')]

dict = {row[0]: row[1] for row in df.itertuples(index=False)}


with open('data/hackers_test/hackers_test_processed.json', 'w', encoding='utf-8') as f:
    f.write(dict_to_json(dict))

def save_words(words, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(words, file, ensure_ascii=False, indent=4)

def add_word(words, word, meaning):
    words[word] = meaning

def remove_word(words, word):
    if word in words:
        del words[word]

def update_word(words, word, meaning):
    if word in words:
        words[word] = meaning

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("src/ui/DataManage.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.button_add)
        self.pushButton_2.clicked.connect(self.button_remove)
    def button_add(self) :
        filename = 'data/hackers_test/hackers_test_processed.json'
        words = json_to_dict('hackers_test')
        word = self.lineEdit.text()
        meaning = self.lineEdit_2.text()
        add_word(words, word, meaning)
        save_words(words, filename)
    def button_remove(self) :
        filename = 'data/hackers_test/hackers_test_processed.json'
        words = json_to_dict('hackers_test')
        word = self.lineEdit.text()
        meaning = self.lineEdit_2.text()
        remove_word(words, word)
        save_words(words, filename)
    def button_update(self) :
        filename = 'data/hackers_test/hackers_test_processed.json'
        words = json_to_dict('hackers_test')
        word = self.lineEdit.text()
        meaning = self.lineEdit_2.text()
        update_word(words, word, meaning)
        save_words(words, filename)

if __name__ == "__main__" :

    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec()

