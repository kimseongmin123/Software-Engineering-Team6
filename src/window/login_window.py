# This Python file uses the following encoding: utf-8
import os
import json
import sys
sys.path.append('.')

from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from src.ui.login_ui import Ui_LoginWindow
from src.module.user_model import *

# ui file to pyqt6 file -> """ python -m PyQt6.uic.pyuic -x example.ui -o example.py """

class LoginWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        self.ui.loginButton.clicked.connect(self.loginFunction)

    def loginFunction(self):
        id = self.ui.id.text()
        pw = self.ui.password.text()
        
        user_list = User.load_users()
        
        if User.get_user(id, user_list) is None:
            QMessageBox.warning(self, '로그인 실패', 'id가 존재하지 않습니다. ')
            return
        user = User.get_user(id, user_list)
        
        if user.check_password(pw) is False:
            print(user.password)
            print(user.hash_password(pw))
            QMessageBox.warning(self, '로그인 실패', '비밀번호가 틀렸습니다. ')
            return
        users = user.update()
        User.save(users)
        QMessageBox.information(self, '로그인 성공', '로그인 성공')
        return

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = LoginWindow()
    widget.show()
    sys.exit(app.exec())




