import json

import sys
from PyQt6.QtWidgets import *
from PyQt6 import uic
import random
sys.path.append('.')

from src.module.data_processing import *

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("src/ui/basic_study.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class BasicStudy(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()

        # UI 파일을 로드합니다.
        uic.loadUi('src/ui/basic_study.ui', self)

        # 단어 리스트 초기화
        self.words = []
        self.i=0
        # JSON 파일에서 단어를 불러옵니다.
        self.load_word_file()
        random.shuffle(self.words)
        self.current_word = None

        # UI 요소를 가져옵니다.
        self.pushButton_before = self.findChild(QPushButton, 'pushButton')
        self.pushButton_after = self.findChild(QPushButton, 'pushButton')
        self.pushButton_main = self.findChild(QPushButton, 'pushButton')
        self.label_eng = self.findChild(QLabel, 'label')
        self.label_kor = self.findChild(QLabel, 'label')

        self.setupUi(self)
        
        if self.words:
            self.i=self.i+1
            self.current_word = self.words[self.i]
            self.label_eng.setText(f"{self.current_word['word']}")
            self.label_kor.setText(f"{self.current_word['meaning']}")

        else:
            QMessageBox.critical(self, "에러", "단어장 파일을 로드해주세요.")

        self.pushButton_before.clicked.connect(self.button_before)
        self.pushButton_after.clicked.connect(self.button_after)
        #self.pushButton_main.clicked.connect(self.button_main)
    def load_word_file(self):
        # 파일 선택 대화 상자를 열어서 JSON 파일을 선택합니다.
        filename, _ = QFileDialog.getOpenFileName(self, "단어장 파일 선택", "", "JSON Files (*.json)")

        if filename:
            # 선택한 파일을 열어서 단어를 로드합니다.
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.words = [{"word": word, "meaning": meaning} for word, meaning in data.items()]

    def button_before(self) :
        if self.i!=0:
            self.i=self.i-1
            self.current_word = self.words[self.i]
            self.label_eng.setText(f"{self.current_word['word']}")
            self.label_kor.setText(f"{self.current_word['meaning']}")
    def button_after(self) :
        if self.words:
            self.i=self.i+1
            self.current_word = self.words[self.i]
            self.label_eng.setText(f"{self.current_word['word']}")
            self.label_kor.setText(f"{self.current_word['meaning']}")

        else:
            QMessageBox.critical(self, "에러", "단어장 파일을 로드해주세요.")
    #def button_main(self) :
    
if __name__ == "__main__" :

    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = BasicStudy() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec()

