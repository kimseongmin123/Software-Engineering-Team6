# This Python file uses the following encoding: utf-8
import os
import json
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_login import Ui_LoginWindow


# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py



class LoginWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        self.loadUsers()
        self.ui.loginButton.clicked.connect(self.loginFunction)

    def loadUsers(self):
        with open('../../userAccount.json') as f:
            self.users = json.load(f)["users"]

    def loginFunction(self):
        inputId = self.ui.id.text()
        inputPassword = self.ui.password.text()

        for user in self.users:
            if (inputId == user['userId']) and (inputPassword == user['userPassword']):
                QMessageBox.information(self, '로그인 성공', '로그인 성공.')
                return

        QMessageBox.warning(self, '로그인 실패', '아이디 또는 비밀번호가 잘못되었습니다.')



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = LoginWindow()
    widget.show()
    sys.exit(app.exec())




