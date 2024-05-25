import sys
import json
import random
from PyQt6 import uic
from PyQt6.QtWidgets import *
from PyQt6.QtCore import QTimer

class EnglishWordGame(QMainWindow):
    def __init__(self):
        super().__init__()

        # UI 파일을 로드합니다.
        uic.loadUi('src/ui/time_attack.ui', self)

        # JSON 파일에서 단어를 불러옵니다.
        self.words = self.load_words_from_json("data/hackers_test/hackers_test_processed.json")

        self.current_word = None
        self.correct_count = 0
        self.is_word_question = True
        self.time_limit = 10
        self.time_left = self.time_limit * 10

        # UI 요소를 가져옵니다.
        self.question_text = self.findChild(QPlainTextEdit, 'plainTextEdit')
        self.answer_input = self.findChild(QLineEdit, 'lineEdit')
        self.submit_button = self.findChild(QPushButton, 'pushButton')
        self.time_progress_bar = self.findChild(QProgressBar, 'progressBar')

        # 버튼 클릭 시 check_answer 함수가 호출
        self.submit_button.clicked.connect(self.check_answer)
        # Enter 키를 누르면 check_answer 함수
        self.answer_input.returnPressed.connect(self.check_answer)

        # 첫 번째 단어를 표시하고 타이머를 시작
        self.next_word()
        self.start_timer()

    def load_words_from_json(self, filename):
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
        return [{"word": word, "meaning": meaning} for word, meaning in data.items()]

    def next_word(self):
        self.current_word = random.choice(self.words)
        self.is_word_question = random.choice([True, False])
        
        if self.is_word_question:
            self.question_text.setPlainText(f"{self.current_word['word']}")
        else:
            self.question_text.setPlainText(f"{self.current_word['meaning']}")

        self.answer_input.clear()

    def start_timer(self):
        self.time_progress_bar.setMaximum(self.time_limit * 1000)  # progress bar의 최댓값을 10초로 설정 (밀리초 단위)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(100)  # 매 0.1초마다 타이머를 업데이트


    def update_timer(self):
        self.time_left -= 1
        progress_percentage = (self.time_left / (self.time_limit * 10)) * 100  # 진행률(백분율) 계산
        progress_value = int(progress_percentage * (self.time_limit * 10))  # 0.1초마다 1%씩 줄어들도록 계산
        self.time_progress_bar.setValue(progress_value)  # ProgressBar 업데이트
        if self.time_left <= 0:
            self.timer.stop()
            self.show_result()

    def check_answer(self):
        answer = self.answer_input.text().strip()
        if (self.is_word_question and answer == self.current_word['meaning']) or \
           (not self.is_word_question and answer == self.current_word['word']):
            self.correct_count += 1
            self.next_word()
        else:
            self.next_word()

    def show_result(self):
        msg = QMessageBox()
        msg.setWindowTitle('결과')
        msg.setText(f"총 맞춘 개수: {self.correct_count}")
        msg.exec()

        self.correct_count = 0
        self.next_word()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = EnglishWordGame()
    game.show()
    sys.exit(app.exec())