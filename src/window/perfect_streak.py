import sys
import json
import random
from PyQt6 import uic
from PyQt6.QtWidgets import *

class EnglishWordGame(QMainWindow):
    def __init__(self):
        super().__init__()

        # UI 파일을 로드합니다.
        uic.loadUi('src/ui/perfect_streak.ui', self)

        # JSON 파일에서 단어를 불러옵니다.
        self.words = self.load_words_from_json("data/hackers_test/hackers_test_processed.json")

        self.current_word = None
        self.correct_count = 0
        self.is_word_question = True

        # UI 요소를 가져옵니다.
        self.question_text = self.findChild(QPlainTextEdit, 'plainTextEdit')
        self.answer_input = self.findChild(QLineEdit, 'lineEdit')
        self.submit_button = self.findChild(QPushButton, 'pushButton')

        # 버튼 클릭 시 check_answer 함수 호출
        self.submit_button.clicked.connect(self.check_answer)

        # Enter 키를 누르면 check_answer 함수 호출
        self.answer_input.returnPressed.connect(self.check_answer)

        # 첫 번째 단어를 표시
        self.next_word()

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

    def check_answer(self):
        answer = self.answer_input.text().strip()
        if (self.is_word_question and answer == self.current_word['meaning']) or \
           (not self.is_word_question and answer == self.current_word['word']):
            self.correct_count += 1
            self.next_word()
        else:
            self.show_result()

    def show_result(self):
        msg = QMessageBox()
        msg.setWindowTitle('결과')
        msg.setText(f"틀렸습니다! 총 맞춘 개수: {self.correct_count}")
        msg.exec()

        self.correct_count = 0
        self.next_word()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = EnglishWordGame()
    game.show()
    sys.exit(app.exec())