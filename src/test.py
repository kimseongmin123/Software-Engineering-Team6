import sys
import json
import random
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox


class WordMeaningTestApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("단어/뜻 테스트 선택")
        self.setGeometry(100, 100, 400, 200)

        self.setup_ui()

    def setup_ui(self):
        self.layout = QVBoxLayout()

        self.word_test_button = QPushButton("단어 테스트", self)
        self.word_test_button.clicked.connect(self.start_word_test)
        self.layout.addWidget(self.word_test_button)

        self.meaning_test_button = QPushButton("뜻 테스트", self)
        self.meaning_test_button.clicked.connect(self.start_meaning_test)
        self.layout.addWidget(self.meaning_test_button)

        self.setLayout(self.layout)

    def start_word_test(self):
        self.word_test_window = WordTestApp()
        self.word_test_window.show()
        self.hide()

    def start_meaning_test(self):
        self.meaning_test_window = MeaningTestApp()
        self.meaning_test_window.show()
        self.hide()


class WordTestApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("단어 테스트")
        self.setGeometry(100, 100, 400, 200)

        self.words = self.load_words_from_json("hackers_test_processed.json")
        self.current_words = []
        self.current_word_index = 0
        self.correct_answers = 0
        self.incorrect_words = []

        self.setup_ui()
        self.start_test()

    def setup_ui(self):
        self.layout = QVBoxLayout()

        self.word_label = QLabel()
        self.layout.addWidget(self.word_label)

        self.answer_input = QLineEdit()
        self.layout.addWidget(self.answer_input)

        self.submit_button = QPushButton("제출", self)
        self.submit_button.clicked.connect(self.check_answer)
        self.layout.addWidget(self.submit_button)

        self.setLayout(self.layout)

    def load_words_from_json(self, filename):
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
        return list(data.items())

    def start_test(self):
        self.current_words = random.sample(self.words, 20)
        self.current_word_index = 0
        self.correct_answers = 0
        self.incorrect_words = []
        self.show_next_word()

    def show_next_word(self):
        if self.current_word_index < len(self.current_words):
            word, meaning = self.current_words[self.current_word_index]
            self.word_label.setText(meaning)
            self.answer_input.clear()
        else:
            self.show_result()

    def check_answer(self):
        if self.current_word_index < len(self.current_words):
            word, meaning = self.current_words[self.current_word_index]
            user_answer = self.answer_input.text().strip().lower()
            if user_answer == word.lower():
                self.correct_answers += 1
            else:
                self.incorrect_words.append((meaning, user_answer))
            self.current_word_index += 1
            self.show_next_word()

    def show_result(self):
        result_message = f"테스트가 종료되었습니다.\n맞은 개수: {self.correct_answers}/{len(self.current_words)}"
        if self.incorrect_words:
            incorrect_word_str = "\n".join(
                [f"{meaning}: {user_answer}" for meaning, user_answer in self.incorrect_words]
            )
            result_message += f"\n\n틀린 문제\n{incorrect_word_str}"
        QMessageBox.information(self, "결과", result_message)
        self.close()
        selection_window.show()


class MeaningTestApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("뜻 테스트")
        self.setGeometry(100, 100, 400, 200)

        self.words = self.load_words_from_json("hackers_test_processed.json")
        self.current_words = []
        self.current_word_index = 0
        self.correct_answers = 0
        self.incorrect_meanings = []

        self.setup_ui()
        self.start_test()

    def setup_ui(self):
        self.layout = QVBoxLayout()

        self.meaning_label = QLabel()
        self.layout.addWidget(self.meaning_label)

        self.answer_input = QLineEdit()
        self.layout.addWidget(self.answer_input)

        self.submit_button = QPushButton("제출", self)
        self.submit_button.clicked.connect(self.check_answer)
        self.layout.addWidget(self.submit_button)

        self.setLayout(self.layout)

    def load_words_from_json(self, filename):
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
        return list(data.items())

    def start_test(self):
        self.current_words = random.sample(self.words, 20)
        self.current_word_index = 0
        self.correct_answers = 0
        self.incorrect_meanings = []
        self.show_next_meaning()

    def show_next_meaning(self):
        if self.current_word_index < len(self.current_words):
            word, meaning = self.current_words[self.current_word_index]
            self.meaning_label.setText(word)
            self.answer_input.clear()
        else:
            self.show_result()

    def check_answer(self):
        if self.current_word_index < len(self.current_words):
            word, meaning = self.current_words[self.current_word_index]
            user_answer = self.answer_input.text().strip().lower()
            if user_answer == meaning.lower():
                self.correct_answers += 1
            else:
                self.incorrect_meanings.append((word, user_answer))
            self.current_word_index += 1
            self.show_next_meaning()

    def show_result(self):
        result_message = f"테스트가 종료되었습니다.\n맞은 개수: {self.correct_answers}/{len(self.current_words)}"
        if self.incorrect_meanings:
            incorrect_meaning_str = "\n".join(
                [f"{word}: {user_answer}" for word, user_answer in self.incorrect_meanings]
            )
            result_message += f"\n\n틀린 문제\n{incorrect_meaning_str}"
        QMessageBox.information(self, "결과", result_message)
        self.close()
        selection_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    selection_window = WordMeaningTestApp()
    selection_window.show()
    sys.exit(app.exec())